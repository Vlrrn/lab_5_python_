#           5
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
    print()
    z = np.arccos(x ** 2) - a * np.sqrt(x) + ((np.sin(np.pi / 2 + a)) ** 3) / np.log10(2 * x)
    return z


print("\n     arccos(x^2) - a*sqrt(x) + sin(pi/2 + a)/log10(2x)\n")
a = check_float("a = ")
while True:
    x = check_float("x = ")
    if 0 < x < 1:
        break
    else:
        print(Fore.RED + "\nНедопустимое значение х!\n" + Style.RESET_ALL)
print("z = %.5f" % function(a, x))
