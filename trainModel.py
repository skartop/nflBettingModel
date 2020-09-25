import keras
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout
from tensorflow.python.keras.callbacks import EarlyStopping
from tensorflow.python.keras.optimizers import RMSprop

dataset = pd.read_csv('data/games/2009.csv', delimiter=',')

for year in range(2008, 2020):
    yeardataset = pd.read_csv('data/games/%d.csv' % year, delimiter=',')
    dataset = pd.concat([dataset, yeardataset])

dataset = dataset.drop(['home_team',
                        'visitor_team',
                        'home_points',
                        'visitor_points',
                        'favorite',
                        'total',
                        'home_margin_of_victory',
                        'over',
                        'date'], axis=1)

cols = dataset.columns.tolist()
cover = cols[2]
spread = cols[1]
rest = cols[3:]
reordered_cols = [cover] + [spread] + rest
dataset = dataset[reordered_cols].to_numpy()

msk = np.random.rand(len(dataset)) < 0.95
train = dataset[msk]
test = dataset[~msk]

X_train = train[:, 1:]
y_train = train[:, 0]
X_test = test[:, 1:]
y_test = test[:, 0]

size = len(X_train[0])

# define the keras model
model = Sequential()
model.add(Dense(128, input_dim=size, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(16, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(2, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(1, activation='sigmoid'))

# compile the keras model
model.compile(loss='mean_absolute_error', optimizer='adam', metrics=['accuracy'])
# model.compile(loss='categorical_crossentropy', optimizer=RMSprop(), metrics=['accuracy'])

# fit the keras model on the dataset
model.fit(X_train, y_train, epochs=500, batch_size=128, validation_data=(X_test, y_test))
# model.fit(X_train, y_train, epochs=500, batch_size=128, validation_data=(X_test,y_test), callbacks=[EarlyStopping(monitor='val_loss', patience=4)])

# evaluate the keras model
oldModel = keras.models.load_model('spreadpredictionmodel')
_, oldAccuracy = oldModel.evaluate(X, y)
_, accuracy = model.evaluate(X_test, y_test)
print('Old Accuracy: %.2f' % (oldAccuracy * 100))
print('Accuracy: %.2f' % (accuracy * 100))

# make class predictions with the model
predictions = model.predict_classes(X_test)
# summarize the first 5 cases
for i in range(15):
    print('%s => %d (expected %d)' % (X_test[i].tolist(), predictions[i], y_test[i]))

if accuracy > oldAccuracy:
    print("replacing old model!")
    model.save('spreadpredictionmodel')
