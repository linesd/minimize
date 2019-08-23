# Minimize [![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/release/python-360/)

This repository is a Python implementation of C.E. Rasmussen's [minimize](http://learning.eng.cam.ac.uk/carl/code/minimize/) function which finds a (local) minimum of a (nonlinear) multivariate function. The function uses conjugate gradients and approximate linesearches based on polynomial interpolation with Wolfe-Powel conditions. The user supplies a function which returns the function value as well as the partial derivatives with respect to the variables to be minimized.

Notes:
- Tested for python >= 3.6

## Usage

Here the two-dimensional [rosenbrock](https://en.wikipedia.org/wiki/Rosenbrock_function) function is used to show how minimize works. The function returns the function value and the partial derivatives with respect to the variables to be minimized.

Starting from initial conditions X0 = np.array([[-1],[0]]) and length = 100 "linesearches":

>> X, convergence, i = minimize(rosenbrock, X0, length=100)

X = array([[1.],
       	   [1.]])

convergence = array([[ 1.04000000e+02, -1.00000000e+00,  0.00000000e+00],
			         [ 2.37965977e+00, -5.16910495e-01,  2.39153220e-01],
			         [ 2.32706339e+00, -5.24606889e-01,  2.70076996e-01],
			         [ 2.29625954e+00, -5.10173722e-01,  2.72781176e-01],
			         [ 1.81191347e+00, -3.05092426e-01,  6.01197093e-02],
			         [ 1.71447070e+00, -2.19978689e-01,  8.38263203e-04],
			         [ 6.91491002e-01,  1.87118858e-01,  1.74877000e-02],
			         [ 6.76960265e-01,  1.78542297e-01,  2.72217021e-02],
			         [ 4.89960939e-01,  3.46292785e-01,  9.48931429e-02],
			         [ 3.51192555e-01,  4.84116914e-01,  2.05204619e-01],
			         [ 2.54267052e-01,  4.96129750e-01,  2.48098759e-01],
			         [ 1.69404850e-01,  6.14217154e-01,  3.62918220e-01],
			         [ 1.16369088e-01,  7.14147306e-01,  4.91389897e-01],
			         [ 6.91860437e-02,  7.37951393e-01,  5.46845078e-01],
			         [ 4.18391999e-02,  8.13230887e-01,  6.53003913e-01],
			         [ 3.04624305e-02,  8.66986583e-01,  7.40365353e-01],
			         [ 1.13408338e-02,  8.96263305e-01,  8.05695260e-01],
			         [ 3.87028837e-03,  9.46723116e-01,  8.93072397e-01],
			         [ 9.20534056e-04,  9.86675590e-01,  9.70802928e-01],
			         [ 2.32598777e-04,  9.84776380e-01,  9.69692858e-01],
			         [ 2.17647876e-06,  9.99792629e-01,  9.99439237e-01],
			         [ 2.39305242e-08,  9.99883820e-01,  9.99777867e-01],
			         [ 2.08976920e-08,  9.99932591e-01,  9.99877974e-01],
			         [ 3.49850571e-09,  9.99940971e-01,  9.99881570e-01],
			         [ 1.46880712e-15,  1.00000000e+00,  1.00000000e+00],
			         [ 3.28531626e-18,  1.00000000e+00,  1.00000000e+00],
			         [ 1.09458505e-20,  1.00000000e+00,  1.00000000e+00],
			         [ 3.45589993e-21,  1.00000000e+00,  1.00000000e+00],
			         [ 3.44606626e-21,  1.00000000e+00,  1.00000000e+00],
			         [ 3.38668373e-21,  1.00000000e+00,  1.00000000e+00],
			         [ 2.51712978e-24,  1.00000000e+00,  1.00000000e+00],
			         [ 4.43734259e-31,  1.00000000e+00,  1.00000000e+00]])

i = 33

The minimum of the function occurs at X = [1., 1.] with a function value of 0 and is determined after 33 iterations. The convergence returned by minimize has the function values in the first column, and the parameters being minimised in the following D columns. If the length parameter is set to a negative value then the algorithm is limited by function evaluations rather than linesearches. The figure shows the result of the above minimization. 

![](imgs/convergence.png)