# Second lesson with keras

import numpy
from keras.datasets import boston_housing
from keras.models import Sequential
from keras.layers import Dense

# for repeat results
numpy.random.seed(42)

# load data
(x_train, y_train), (x_test, y_test) = boston_housing.load_data()

# standardisation data
mean = x_train.mean(axis=0)
std = x_train.std(axis=0)
x_train -= mean
x_train /= std
x_test -= mean
x_test /=std

# create neural network
model = Sequential()

model.add(Dense(128, activation='relu', input_shape=(x_train.shape[1],)))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

model.fit(x_train, y_train, epochs=10, batch_size=1, verbose=1)

mse, mae = model.evaluate(x_test, y_test, verbose=0)
print(mae)

pred = model.predict(x_test)

# compare data test and train
print(pred[1][0], y_test[1])
print(pred[50][0], y_test[50])
print(pred[100][0], y_test[100])