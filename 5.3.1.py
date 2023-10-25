import numpy as np
from matplotlib import pyplot as plt


def fun(a):
    y = (np.cos(3.567) / np.sin(3.567)) ** 3 + 2.24 * a * 3.567
    return y


def fun2(a):
    return a


title_font = {"fontsize": 25, "color": "#00A693"}
label_font = {"fontsize": 12, "color": "#075878"}
legend_font = {"size": 10}
arr = np.arange(-5, 12.1, 0.5)
s = arr.size
list_ = []
list_m = []
for i in arr:
    f = fun(i)
    list_.append(f)
    print(" x = ", i, "     f(x) = ", f)
f_x = np.array(list_).reshape(s, 1)
print(f_x)
m = f_x.mean()
for i in arr:
    f2 = fun2(m)
    list_m.append(f2)
f_m = np.array(list_m)
print("min = ", f_x.min(), "\nmax = ", f_x.max(), "\nmean = ", m, "\ncol = ", s)
f1 = np.sort(f_x, axis=0)
print(f1)
plt.plot(arr, f_x, label="f(x)", color="#106cc2", marker="*")
plt.plot(arr, f_m, label="mean", color="#00A693", marker="8")
plt.title("Графики", fontdict=title_font)
plt.xlabel("Переменая x", fontdict=label_font)
plt.ylabel("Функция f(x)", fontdict=label_font)
legend = plt.legend(loc="lower right", prop=legend_font)
plt.setp(legend.get_texts(), color="#8c0a8c")
plt.show()