# 3 lesson how to SAVE and LOAD train network

import numpy

from keras.datasets import mnist
from keras.models import Sequential
from keras.models import model_from_json
from keras.layers import Dense
from keras.utils import np_utils

numpy.random.seed(42)

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)

X_train = X_train.astype('float32')
X_train /= 255
X_test = X_test.astype('float32')
X_test /= 255

Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)

model = Sequential()


#  1 layer
model.add(Dense(800, input_dim=784, init="normal", activation="relu"))
# 2 layer
model.add(Dense(10, init="normal", activation="softmax"))

model.compile(loss="categorical_crossentropy", optimizer="SGD", metrics=["accuracy"])
# learn
model.fit(X_train, Y_train, batch_size=200, nb_epoch=10,  validation_split=0.2, verbose=1)
scores = model.evaluate(X_test, Y_test, verbose=0)
print("ПЕРВЫЙ Точность работы на тестовых данных: %.2f%%" % (scores[1]*100))

# save model
model_json = model.to_json()

# save struct of network to file
json_file = open("../data/saves/mnist_model.json", "w")
json_file.write(model_json)
json_file.close()

# save weight
model.save_weights("../data/saves/mnist_model.h5")


# open struct of network to file
json_file = open("../data/saves/mnist_model.json", "r")
loaded_model_json = json_file.read()
json_file.close()



# create model with struck
loaded_model = model_from_json(loaded_model_json)

# load weight
loaded_model.load_weights("../data/saves/mnist_model.h5")
loaded_model.compile(loss="categorical_crossentropy", optimizer="SGD", metrics=["accuracy"])

print(loaded_model.summary())

scores = loaded_model.evaluate(X_test, Y_test, verbose=0)
print("ЗАГРУЖЕННЫЙ Точность работы на тестовых данных: %.2f%%" % (scores[1]*100))