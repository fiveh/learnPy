# first try to USE CNN mnist for search number

import numpy as np
from keras.utils import np_utils
from keras.models import model_from_json
from keras.preprocessing import image
from keras.datasets import mnist
import matplotlib.pyplot as plt

json_file = open("../data/saves/mnist_model_for_img.json", "r")
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("../data/saves/mnist_model_for_img.h5")

loaded_model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

img_path = "../data/images/1.png"
img = image.load_img(img_path, target_size=(28, 28), grayscale=True)
plt.imshow(img, cmap='gray')
plt.show()

x = image.img_to_array(img)
x = 255 - x
x /= 255
x = np.expand_dims(x, axis=0)

print(x.shape)

prediction = loaded_model.predict(x)

prediction = np_utils.np.argmax(prediction, axis=1)
print("\nResult is:", prediction)



