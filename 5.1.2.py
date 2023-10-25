#           5
#  А = (X^T * X)^(-1) * (X^T * Y)
#  y = a0 + a1x1 + a2x2

import numpy as np
import random

x = np.ones((12, 1), dtype=np.int32)
x = np.concatenate((x, np.random.randint(5, 17, (12, 1)), np.random.randint(60, 82, (12, 1))), axis=1)
print("X:\n", x)
y = np.array([random.uniform(13.5, 18.6) for i in range(12)]).reshape(12, 1)
print("Y:\n", y)
a = (np.linalg.inv(x.T @ x)) @ (x.T @ y)
print("A:\n", a)
print("Y (МНК):")
a_list = []
for i in x:
    y_i = 0
    for i1, i2 in zip(i, a):
        y_i += i1 * i2
    a_list.append(y_i)
new_y = np.array(a_list)
print(new_y)
print("Y-Y\n", np.subtract(y, new_y))
