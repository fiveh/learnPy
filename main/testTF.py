import tensorflow as tf
import keras as kf


hello = tf.constant('hello world from tf')
sess = tf.Session()
print(sess.run(hello))

