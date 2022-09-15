# Пятая программа второй практической работы
# В данной программе проверяется возможность загрузки
# данных по домам в Калифорнии с помощью пакета sklearn
import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing

# Пятое задание - установка и запись данных о домах в Калифорнии
california_housing = fetch_california_housing()

california_housing_data = pd.DataFrame(data=california_housing.data,
                                       columns=california_housing.feature_names)
california_housing_target = pd.DataFrame(data=california_housing.target,
                                         columns=california_housing.target_names)

# Шестое задание - соединение двух таблиц в единую таблицу
print("\n\nШестое задание:\n")
concatenatedTab = pd.concat([california_housing_data, california_housing_target], axis=1)
print("ID", concatenatedTab)

# Седьмое задание - использование метода info()
print("\n\nСедьмое задание:\n")
print(california_housing_data.info())

# Восьмое задание - проверка пустых ячеек в таблицах
print("\n\nВосьмое задание:\n")
print(california_housing_data.isna().sum(),
      california_housing_target.isna().sum(), sep='\n')

# Девятое задание - вывод зданий старше 50 лет с численностью населения
# больше 2500 человек, используя метод loc()
print("\n\nДевятое задание:\n")
requirement1 = concatenatedTab['HouseAge'].values > 50
requirement2 = concatenatedTab.loc[requirement1]
requirement3 = requirement2['Population'].values > 2500

newConcatenatedTab = requirement2.loc[requirement3]
print(newConcatenatedTab)

# Десятое задание - поиск максимального и минимального значения
# медианой стоимости дома
print("\n\nДесятое задание:\n")
print(california_housing_target.max(),
      california_housing_target.min(), sep='\n')

# Одиннадцатое задание - вывод названия признака и его среднего
# значения, используя метод apply()
print("\n\nОдиннадцатое задание:\n")
print(california_housing_data.apply(np.mean, axis=0))
