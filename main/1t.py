import numpy

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
from sympy.simplify.tests.test_cse import opt1

numpy.random.seed(42)

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(60000, 784)

X_train = X_train.astype('float32')
X_train /= 255

y_train = np_utils.to_categorical(y_train, 10)

model = Sequential()


# 1 layer
model.add(Dense(800, input_dim=784, init="normal", activation="relu"))
# 2 layer
model.add(Dense(10, init="normal", activation="softmax"))


model.compile(loss="categorical_crossentropy", optimizer="SGD", metrics=["accuracy"])
print(model.summary())