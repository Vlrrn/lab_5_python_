import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def data1():
    x = np.linspace(0, 10, 100)
    y = np.linspace(0, 10, 100)
    x_grid, y_grid = np.meshgrid(x, y)
    z = x_grid ** 0.25 + y_grid ** 0.25
    return x_grid, y_grid, z


def data2():
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    x_grid, y_grid = np.meshgrid(x, y)
    z = x_grid ** 2 - y_grid ** 2
    return x_grid, y_grid, z


def data3():
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    x_grid, y_grid = np.meshgrid(x, y)
    z = x_grid * 2 - y_grid * 3
    return x_grid, y_grid, z


def data4():
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    x_grid, y_grid = np.meshgrid(x, y)
    z = x_grid ** 2 - y_grid ** 3
    return x_grid, y_grid, z


def data5():
    x = np.linspace(-2, 2, 100)
    y = np.linspace(-2, 2, 1000)
    x_grid, y_grid = np.meshgrid(x, y)
    z = 2 + 2 * x_grid + 2 * y_grid - x_grid ** 2 - y_grid ** 2
    return x_grid, y_grid, z


x1, y1, z1 = data1()
x2, y2, z2 = data2()
x3, y3, z3 = data3()
x4, y4, z4 = data4()
x5, y5, z5 = data5()
fgr = plt.figure()
ax1 = fgr.add_subplot(3, 3, 1, projection='3d')
ax2 = fgr.add_subplot(3, 3, 3, projection='3d')
ax3 = fgr.add_subplot(3, 3, 5, projection='3d')
ax4 = fgr.add_subplot(3, 3, 7, projection='3d')
ax5 = fgr.add_subplot(3, 3, 9, projection='3d')
ax1.plot_surface(x1, y1, z1, cmap='Spectral')
ax2.plot_surface(x2, y2, z2, cmap='Spectral')
ax3.plot_surface(x3, y3, z3, cmap='Spectral')
ax4.plot_surface(x4, y4, z4, cmap='Spectral')
ax5.plot_surface(x5, y5, z5, cmap='Spectral')
plt.show()
