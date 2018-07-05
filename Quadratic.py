import tensorflow as tf
a = tf.constant(2.0)
b = tf.constant(1.0)
c = tf.constant(1.0)
x = tf.Variable(10.0, trainable=True)
LR = 0.01 #Learning Rate
y = a * x* x - b *x - c #2x^2 - x - 1
#One of the solution is x = 1 which we are going to compute
optAdam = tf.train.AdamOptimizer(LR).minimize(y)
optGD = tf.train.GradientDescentOptimizer(LR).minimize(y)
#We will compute such that y = 0
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for i in range(10000):
        print(sess.run([x,y]))
        sess.run(optAdam)
        if(sess.run(y) < 0):

            break

with tf.Session() as sess1:
    sess1.run(init)
    for i in range(10000):
        print(sess1.run([x,y]))
        sess1.run(optGD)
        if(sess1.run(y) < 0):
            break
