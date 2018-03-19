# analyse with IMDB dataset

import numpy as np
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Activation, Embedding
from keras.layers import LSTM
from keras.datasets import imdb

# set 'seed' for repeat
np.random.seed(42)

# max count words
max_features = 5000

# load data
(X_train, y_train), (X_test, y_test) = imdb.load_data(nb_words=max_features)

# max size recension in words
maxlen = 80

# add or cut recension
X_train = sequence.pad_sequences(X_train, maxlen=maxlen)
X_test = sequence.pad_sequences(X_test, maxlen=maxlen)

# create network
model = Sequential()

# layer for vectoring interpretation words
model.add(Embedding(max_features, 32, dropout=0.2))
# long-short temp memory
model.add(LSTM(100, dropout_W=0.2, dropout_U=0.2))
# full connected layer
model.add(Dense(1, activation="sigmoid"))

# compile network
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# train network
model.fit(X_train, y_train, batch_size=64, epochs=7, validation_data=(X_test, y_test), verbose=1)

# check train
scores = model.evaluate(X_test, y_test, batch_size=64)
print("Accurasy on test data: %.2f%%" % (scores[1]*100))