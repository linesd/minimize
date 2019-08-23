import numpy as np
from check_grad import check_grad
from rosenbrock import rosenbrock
from rosenbrock_with_args import rosenbrock_with_args

np.random.seed(0)
X = np.random.normal(0, 1, size=(3,1))
d1 = check_grad(rosenbrock, X, 1e-5)
print("d1 : ", d1)

d2 = check_grad(rosenbrock_with_args, X, 1e-5, args=(100, 400))
print("d2 : ", d2)