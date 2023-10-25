import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

pp = pd.read_csv("price_prepared.csv", sep=';', nrows=1000)
print(pp)
pp.info()
print('\n', pp.describe(include='all'))
data_c = np.array(pp.columns)
print(data_c)
fgr = plt.figure(figsize=(12, 10))
for i in range(5):
    ax = fgr.add_subplot(3, 3, 2 * i + 1)
    plt.title("{}".format(data_c[i]))
    ax.hist(pp[data_c[i]])
plt.show()