# TensorFlow-Basics-Solving-Quadratic-Equation
Tensorflow is a library that support mathematical models in an efficient manner and is used mainly for neural network applications such as Machine Learning. It is developed by google and is available as an open source API in both python and C. It is now the most popular library used to develop Deep learning models as it provides large amount of functions to work on. It uses a Graph based approach to compute the variables and operations related to it. These graph are executed in a session which contains the variables and constants.

In this project let us create a python script that uses tensorflow library to solve a quadratic equation. The objective is to understand the working of Adam optimizer to minimize loss and the way learning rate effects the loss outcome.

ADAM Optimizer
Adam optimizer is modified version of stochastic gradient descent in which update of parameters occurs at every iteration.  It became popular as it was specifically developed to optimize the loss for training large amount of data.

The main aim of using gradients is to update the parameters (Such as weights and bias in neural networks). Adam optimizer is implemented by combing RMSProp and Gradient Descent with momentum. Gradient descent is a fast algorithm but not accurate enough. Adam improvised the accuracy but it is computational expensive as it has to maintain the moving averages and variances at every iteration.

Some of the advantages of using Adam optimizer are:

One value of Learning rate is used
The oscillation during gradient descent is reduced hence the convergence is more accurate
Fewer hyper parameters to work on

Learning Rate
One of the way to improvise the optimization is to use learning rate. If it is faster, then convergence will have large steps towards the minimum function, produces oscillation . In most case performance may diverge. And if learning rate is slow the convergence will not be accurate.
