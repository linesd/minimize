import numpy as np

def rosenbrock_with_args(x, a, b):
	"""
	This function function returns the function value and partial 
	derivatives of the general dimension rosenbrock function, given by:

		f(x) = sum_{i=1:D-1} 100*(x(i+1) - x(i)^2)^2 + (1-x(i))^2 

	where D is the dimension of x.

	The true minimum of the function is 0 at x = (1 1 ... 1)

	Parameters
	----------

	x : parameter of the function

	returns
	-------

	f : function value

	df : partial derivatives wrt x_i

	"""
	D = len(x) 
	# function
	f = np.sum( a * (x[1:D] - x[:D-1] ** 2) ** 2 + (1 - x[:D-1]) ** 2 )
	# partial derivatives
	df = np.zeros((D,1))
	df[:D-1] = -b * x[:D-1] * (x[1:D] - x[:D-1] ** 2) - 2 * (1 - x[:D-1])
	df[1:D] += 200 * (x[1:D] - x[:D-1] ** 2)

	return f, df