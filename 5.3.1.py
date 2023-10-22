import numpy as np
from matplotlib import pyplot as plt


def fun(a):
    y = (np.cos(3.567) / np.sin(3.567)) ** 3 + 2.24 * a * 3.567
    return y


arr = np.arange(-5, 12.1, 0.5)
s = arr.size
list_ = []
for i in arr:
    f = fun(i)
    list_.append(f)
    print(" x = ", i, "     f(x) = ", f)
f_x = np.array(list_).reshape(s, 1)
print(f_x)
m = f_x.mean()
print("min = ", f_x.min(), "\nmax = ", f_x.max(), "\nmean = ",m, "\ncol = ", s)
f1 = np.sort(f_x, axis=0)
print(f1)
plt.plot(arr, f_x, label="f(x)")
plt.plot([arr[0], arr[-1]], [m, m], label="mean", color="#00A693", linestyle="dashed")
plt.title(
    "Графики",
    fontsize=25,
    color="#00A693")
plt.xlabel("Переменая x")
plt.ylabel("Функция f(x)")
plt.legend()
plt.show()