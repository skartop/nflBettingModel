import keras
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
from tensorflow.python.keras.callbacks import EarlyStopping
from tensorflow.python.keras.optimizer_v2.rmsprop import RMSprop

dataset = pd.read_csv('data/games/2007.csv', delimiter=',')

for year in range(2008, 2020):
    yeardataset = pd.read_csv('data/games/%d.csv' % year, delimiter=',')
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

cols = dataset.columns.tolist()
cover = cols[2]
spread = cols[1]
rest = cols[3:]
reordered_cols = [cover] + [spread] + rest
dataset = dataset[reordered_cols].to_numpy()

X = dataset[:, 1:]
y = dataset[:, 0]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=1)


size = len(X_train[0])

# define the keras model
model = Sequential()
model.add(Dense(128, input_dim=size, activation='selu'))
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
model.compile(optimizer=RMSprop(), loss='binary_crossentropy', metrics=['BinaryAccuracy'])

# fit the keras model on the dataset
# model.fit(X_train, y_train, epochs=500, batch_size=128, validation_data=(X_test, y_test))
model.fit(X_train, y_train, epochs=1500, batch_size=50, validation_data=(X_test, y_test),
          callbacks=[EarlyStopping(monitor='binary_accuracy', patience=10)])

# evaluate the keras model
oldModel = keras.models.load_model('model/spreadpredictionmodel')
_, oldAccuracy = oldModel.evaluate(X_val, y_val)
_, accuracy = model.evaluate(X_val, y_val)
print('Old Accuracy: %.2f' % (oldAccuracy * 100))
print('Accuracy: %.2f' % (accuracy * 100))

# make class predictions with the model
predictions = model.predict_classes(X_test)
# summarize the first 5 cases
for i in range(15):
    print('%s => %d (expected %d)' % (X_test[i].tolist(), predictions[i], y_test[i]))

if accuracy > oldAccuracy:
    print("replacing old model!")
    model.save('model/spreadpredictionmodel')
