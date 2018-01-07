# CNN mnist

import numpy
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers.convolutional import MaxPooling2D, Conv2D
from keras.utils import np_utils

# for repeat
numpy.random.seed(42)

# image size
img_rows, img_cols = 28, 28

# load data
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# transform dimension image
X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols, 1)
X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1)
input_shape = (img_rows, img_cols, 1)

# normalisation data from 0 to 1
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

# transform label to category
Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)

# create model
model = Sequential()

# 1 convolution layer
model.add(Conv2D(75, kernel_size=(5, 5), input_shape=input_shape, activation='relu'))
# first sub-layer
model.add(MaxPooling2D(pool_size=(2, 2)))
# regularisation layer
model.add(Dropout(0.2))
# 2 convolution layer
model.add(Conv2D(100, (5, 5), activation='relu'))
# second sub-layer
model.add(MaxPooling2D(pool_size=(2, 2)))
# regularisation layer
model.add(Dropout(0.2))
# transformation from 2d to 1d
model.add(Flatten())
# full-connected layer
model.add(Dense(500, activation='relu'))
# regularisation layer
model.add(Dropout(0.5))
# output layer
model.add(Dense(10, activation='softmax'))

# compile network
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# train network
model.fit(X_train, Y_train, batch_size=200, epochs=10, validation_split=0.2, verbose=2)

# save model
model_json = model.to_json()

# save struct of network to file
json_file = open("../data/saves/mnist_model_for_img.json", "w")
json_file.write(model_json)
json_file.close()

# save weight
model.save_weights("../data/saves/mnist_model_for_img.h5")

# check how correct our train on 'tests data'
scores = model.evaluate(X_test, Y_test, verbose=0)
print("Exactly work on test data: %.2f%%" % (scores[1]*100))























