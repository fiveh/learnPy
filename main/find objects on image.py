# first try to USE CNN cifar-10 to search objects on image

import numpy as np
from keras.utils import np_utils
from keras.models import model_from_json
from keras.preprocessing import image
from keras.optimizers import SGD
import matplotlib.pyplot as plt

# load model and weights
json_file = open("../data/saves/cifar10_model.json", "r")
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("../data/saves/cifar10_weights.h5")

# compile model
loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# names of classes
classes = ['самолет', 'автомобиль', 'птица', 'кот', 'олень', 'собака', 'лягушка', 'лошадь', 'корабль', 'грузовик']

# load image
img_path = "../data/images/p4.jpg"
img = image.load_img(img_path, target_size=(32, 32))
plt.imshow(img)
plt.show()

# transform img to array
x = image.img_to_array(img)
x /= 255
x = np.expand_dims(x, axis=0)

# run search
prediction = loaded_model.predict(x)
prediction = np_utils.np.argmax(prediction, axis=1)
print(classes[prediction[0]])