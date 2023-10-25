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


data = [data1(), data2(), data3(), data4(), data5()]
fgr = plt.figure(figsize=(12, 10))
for i in range(5):
    ax = fgr.add_subplot(3, 3, 2 * i + 1,  projection='3d')
    plt.title("{}".format(i+1))
    ax.plot_surface(data[i][0], data[i][1], data[i][2], cmap='Spectral')
plt.show()
