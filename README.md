# Minimize [![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/release/python-360/)

This repository is a Python implementation of C.E. Rasmussen's [minimize](http://learning.eng.cam.ac.uk/carl/code/minimize/) function which finds a (local) minimum of a (nonlinear) multivariate function. The function uses conjugate gradients and approximate linesearches based on polynomial interpolation with Wolfe-Powel conditions. The user supplies a function which returns the function value as well as the partial derivatives with respect to the variables to be minimized.

Notes:
- Tested for python >= 3.6

## Usage

Here the two-dimensional [rosenbrock](https://en.wikipedia.org/wiki/Rosenbrock_function) function is used to show how minimize works. The function returns the function value and the partial derivatives with respect to the variables to be minimized.

Starting from initial conditions X0 = np.array([[-1],[0]]) and length = 100 "linesearches":

>>> X, convergence, i = minimize(rosenbrock, X0, length=100)

>>> X  
array([[1.],
   	   [1.]])

>>> i 
33

The minimum of the function occurs at X = [1., 1.] with a function value of 0 and is determined after 33 iterations. The convergence returned by minimize has the function evaluations in the first column, and the parameters being minimised in the following D columns. The figure below shows the convergence values plotted over the rosenbrock function. If the length parameter is set to a negative value then the algorithm is limited by function evaluations rather than linesearches. 
![](img/convergence.png)