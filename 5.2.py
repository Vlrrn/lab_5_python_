# 1.	\Импортировать датасет.
# 2.	\Взять 1000 значений из выбранного датасета.
# 3.	\Проверить данные на пропуски.
# 4.	\Проверить на нормальность распределения и выбросы. Использовать для проверки нормальности распределения ящики с усами (логарифмическую шкалу) и гистограммы.
# 5.	\Заполнить пропуски и обработать аномальные значения.
# 6.	\Определить сколько в выборке 1, 2, 3 …комнатных квартир.
# 7.	\Построить сводную таблицу: подписи строк – районы, подписи колонок – комнаты, пересечение строк и столбцов – количество квартир в этом районе.
# 8.	\Итоговый обработанный массив без выбросов и пропусков сохраните в файл surname.csv
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def plots(pp, data_c):
    fgr = plt.figure(figsize=(12, 10))
    for i in range(len(data_c)):
        ax1 = fgr.add_subplot(7, 6, 2 * i + 1)
        plt.title("{}".format(data_c[i]))
        ax2 = fgr.add_subplot(7, 6, 2 * i + 2)
        fgr.subplots_adjust(wspace=0.5, hspace=0.8)
        ax1.hist(pp[data_c[i]], bins=20)
        try:
            ax2.boxplot(pp[data_c[i]])
        except TypeError:
            print("...", data_c[i])
    plt.show()


def main():
    pp = pd.read_csv("test.csv", sep=',', nrows=1000)
    print(pp)
    print('\n', pp.describe(include='all'))
    print('\nПропущенные значения:\n')
    print(pp.isnull().sum(), '\n')
    data_c = np.array(pp.columns)
    numeric_cols = pp.select_dtypes(include=[np.number]).columns.values
    non_numeric_cols = pp.select_dtypes(exclude=[np.number]).columns.values
    plots(pp, data_c)
    for col in non_numeric_cols:            # преобразование типов
        pp.loc[pp[col] == 'A', col] = '1'
        pp.loc[pp[col] == 'B', col] = '2'
    for col in data_c:
        pp[col] = pp[col].astype(float)
    print("\nТипы преобразованы.\n")
    plots(pp, data_c)
    print()
    for col in data_c:                      # заполнение пропущенных за=начений
        # pp.dropna(axis='index', subset=[col], inplace=True)
        if np.sum(pp[col].isnull()):
           pp[col].fillna(pp[col].median(), inplace=True)
    print("Пропуски заполнены.\n")
    print(pp.isnull().sum())
    rooms = pp["Rooms"].value_counts()
    r1, r2, r3 = rooms[1], rooms[2], rooms[3]
    str_rooms = 'комнатных'
    print(f'\nКоличество квартир:\n\n1-{str_rooms} : {r1}\n2-{str_rooms} : {r2}\n3-{str_rooms} : {r3}\n\n')
    plots(pp, data_c)
    for col in numeric_cols:
        low = pp[col].quantile(q=0.25)
        upp = pp[col].quantile(q=0.75)
        iqr = upp - low
        pp.loc[(pp[col] < low - 1.5 * iqr) | (pp[col] > upp + 1.5 * iqr), col] = pp[col].mean()
    for col in numeric_cols:
        low = pp[col].quantile(q=0.25)
        upp = pp[col].quantile(q=0.75)
        iqr = upp - low
        pp.loc[(pp[col] < low - 1.5 * iqr) | (pp[col] > upp + 1.5 * iqr), col] = pp[col].median()
    print("Выбросы обработаны.\n\n")
    pp.info()
    print()
    plots(pp, data_c)
        # подписи строк – районы,
        # подписи колонок – комнаты,
        # пересечение строк и столбцов – количество квартир в этом районе
    pp.insert(0, 'Quantity', np.ones((len(pp), 1)))
    pp['Quantity'] = pp['Quantity'].astype(float)
    print(pp)
    print("\nСводная таблица:\n")
    # tab_ = pp.pivot_table(pp, index=['DistrictId'], columns=['Rooms'], values=['Quantity'], aggfunc=[np.sum], fill_value=0)
    tab_ = pd.pivot_table(pp, index=['DistrictId', 'Rooms'], values=['Quantity'], aggfunc=[np.sum], fill_value=0)
    print(tab_)
    pp.to_csv('surname.csv', index=False)
    pp1 = pd.read_csv('surname.csv')
    print(pp1)


if __name__ == '__main__':
    main()