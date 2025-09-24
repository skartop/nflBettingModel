import os

import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import RMSprop

dataset = pd.read_csv('data/games/2007.csv', delimiter=',')

for year in range(2008, 2020):
    year_path = 'data/games/%d.csv' % year
    if not os.path.exists(year_path):
        print("Skipping missing data file:", year_path)
        continue
    yeardataset = pd.read_csv(year_path, delimiter=',')
    dataset = pd.concat([dataset, yeardataset])

dataset = dataset.drop(['date',
                        'home_team',
                        'visitor_team',
                        'home_points',
                        'visitor_points',
                        'home_margin_of_victory',
                        'favorite',
                        'total',
                        'over'], axis=1)

dataset = dataset.loc[:, ~dataset.columns.str.contains('^Unnamed')]

feature_cols = [col for col in dataset.columns if col != 'cover']
X = dataset[feature_cols].to_numpy(dtype=np.float32)
y = dataset['cover'].to_numpy(dtype=np.float32)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=1)


size = len(X_train[0])

# define the keras model
model = Sequential()
model.add(Dense(128, activation='selu', input_shape=(size,)))
model.add(Dropout(0.1))
model.add(Dense(128, activation='selu'))
model.add(Dropout(0.1))
model.add(Dense(64, activation='selu'))
model.add(Dropout(0.1))
model.add(Dense(32, activation='selu'))
model.add(Dropout(0.1))
model.add(Dense(16, activation='selu'))
model.add(Dropout(0.1))
model.add(Dense(2, activation='selu'))
model.add(Dropout(0.1))
model.add(Dense(1, activation='sigmoid'))

# compile the keras model
# model.compile(loss='mean_absolute_error', optimizer='adam', metrics=['accuracy'])
# model.compile(loss='categorical_crossentropy', optimizer=RMSprop(), metrics=['accuracy'])
model.compile(optimizer=RMSprop(), loss='binary_crossentropy', metrics=['binary_accuracy'])

# fit the keras model on the dataset
# model.fit(X_train, y_train, epochs=500, batch_size=128, validation_data=(X_test, y_test))
model.fit(
    X_train,
    y_train,
    epochs=1500,
    batch_size=50,
    validation_data=(X_test, y_test),
    callbacks=[EarlyStopping(monitor='val_binary_accuracy', patience=10, restore_best_weights=True)],
    verbose=1,
)

# evaluate the keras model
model_path = 'model/spreadpredictionmodel.keras'

oldAccuracy = None
if tf.io.gfile.exists(model_path):
    try:
        old_model = tf.keras.models.load_model(model_path)
        _, oldAccuracy = old_model.evaluate(X_val, y_val, verbose=0)
        print('Old Accuracy: %.2f' % (oldAccuracy * 100))
    except Exception as exc:
        print(f"Unable to load existing model for comparison: {exc}")

_, accuracy = model.evaluate(X_val, y_val, verbose=0)
print('New Accuracy: %.2f' % (accuracy * 100))

# make class predictions with the model
predictions = (model.predict(X_test, verbose=0) > 0.5).astype("int32").flatten()
# summarize the first 5 cases
for i in range(15):
    print('%s => %d (expected %d)' % (X_test[i].tolist(), predictions[i], y_test[i]))

if oldAccuracy is None or accuracy > oldAccuracy:
    print("Replacing saved model with new weights.")
    model.save(model_path)
else:
    print("Kept existing model; new model underperformed.")
