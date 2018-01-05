# convolution neural network with dataset: "cifar-10"

import numpy
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Flatten, Activation
from keras.layers import Dropout
from keras.layers.convolutional import Convolution2D, MaxPooling2D, Conv2D
from keras.utils import np_utils

# for repeat
numpy.random.seed(42)

# load data
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

# normalisation data from 0 to 1
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)

# create model
model = Sequential()

# 1 convolution layer
model.add(Conv2D(32, (3, 3), padding='same', input_shape=(32, 32, 3), activation='relu'))
# 2 convolution layer
model.add(Conv2D(32, (3, 3), activation='relu'))
# first sub-layer
model.add(MaxPooling2D(pool_size=(2, 2)))
# regularisation layer
model.add(Dropout(0.25))
# 3 convolution layer
model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
# 4 convolution layer
model.add(Conv2D(64, (3, 3), activation='relu'))
# second sub-layer
model.add(MaxPooling2D(pool_size=(2, 2)))
# regularisation layer
model.add(Dropout(0.25))
# transformation from 2d to 1d
model.add(Flatten())
# full-connected layer
model.add(Dense(512, activation='relu'))
# regularisation layer
model.add(Dropout(0.5))
# output layer
model.add(Dense(10, activation='softmax'))

# compile network
model.compile(loss='categorical_crossentropy', optimizer='SGD', metrics=['accuracy'])

# need to try run 25 epochs for good result
# train network
model.fit(X_train, Y_train, batch_size=32, epochs=5, validation_split=0.1, shuffle=True)

# check how correct our train on 'tests data'
scores = model.evaluate(X_test, Y_test, verbose=0)
print("Exactly work on test data: %.2f%%" % (scores[1]*100))























