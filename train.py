''' Adapted from
https://www.tensorflow.org/get_started/mnist/beginners
'''

# Downloading MNIST data
from tensorflow.examples.tutorials.mnist import input_data
# Importing the data, one hot seperates the data into matrices and each matrix will
# have only one '1' value, this will enable the machine to read without using words
data = input_data.read_data_sets("MNIST_data/", one_hot=True)

import tensorflow as tf

# Flattening each image into 784-dimensional vector, None means the dimension can be any length, 2-D tensor
# of floating point numbers
x = tf.placeholder(tf.float32, [None, 784])

# Creating the Variables and filling them with 0's as these are going to be trained
weights = tf.Variable(tf.zeros([784, 10]))
biases = tf.Variable(tf.zeros([10]))

# Implementation of model
y = tf.nn.softmax(tf.matmul(x, weights) + biases)

# Creating new placeholder to input correct answers and then implemting cross_entropy function
y_ = tf.placeholder(tf.float32, [None,10])
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

# Training, using Gradient Descent to minimise loss
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
# Launching model
sess = tf.InteractiveSession()
# Initialise variables created
tf.global_variables_initializer().run()

# Loop and batch read images and add to session
for i in range(1000):
    batch_xs, batch_ys = data.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

# Check to see if prediction matches are correct
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# Print accuracy
print(sess.run(accuracy, feed_dict={x: data.test.images, y_: data.test.labels}))