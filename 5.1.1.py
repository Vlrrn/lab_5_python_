#                       5 вариант

import numpy as np
import colorama
from colorama import Fore, Style

colorama.init()


def check_float(s):
    while True:
        try:
            f = float(input(s))
            return f
        except ValueError:
            print(Fore.RED + "\nВведите число!\n" + Style.RESET_ALL)


def function(a, x):
    z = np.arccos(x ** 2) - a * np.sqrt(x) + ((np.sin(np.pi / 2 + a)) ** 3) / np.log10(2 * x)
    return z


a = check_float("a = ")
x = check_float("x = ")
print("z = %.5f" % function(a, x))