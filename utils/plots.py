import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_2d_function_convergence(X, Y, Z, convergence, path=None):

    # plot data
    fig = plt.figure(figsize=(8,6))
    ax = plt.axes(projection='3d')

    ax.view_init(elev=45., azim=45)
    ax.plot(convergence[:,1], convergence[:,2], convergence[:,0], '-r*', markersize=12)
    ax.scatter(1, 1, 0, s=100)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis',
                    edgecolor='none', alpha=0.3, antialiased=False)
    ax.set_xlabel('$X_{1}$', fontsize=20)
    ax.set_ylabel('$X_{2}$', fontsize=20)
    ax.set_zlabel('$f(\mathbf{X})$', fontsize=20)

    if path is not None:
        plt.savefig(path, dpi=200)

    plt.show()