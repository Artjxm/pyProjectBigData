import pandas as pd
import numpy as np
import scipy.stats as sts

data = pd.read_csv('ECDCCases.csv', sep=',')


# Первое задание шестой практической работы
def task1():
    print('\nВыполнение первого задания:\n', data, '\n\n')


# Второе задание шестой практической работы
def task2():
    print('Выполнение второго задания:\n\nДанные до обработки:')
    for column in data.columns:
        missing = np.mean(data[column].isna() * 100)
        print(column, ": ", round(missing, 1), "%")

    # Удаление двух признаков из датасета
    data.drop('geoId', axis=1, inplace=True)
    data.drop('Cumulative_number_for_14_days_of_COVID-19_cases_per_100000',
              axis=1,
              inplace=True)

    # Заполнение рядов медианой столбца данных либо
    # 'other' для текстовых показателей
    data.popData2019.fillna(data.popData2019.median(), inplace=True)
    data.countryterritoryCode.fillna('other', inplace=True)

    print('\nДанные после обработки:')
    for column in data.columns:
        missing = np.mean(data[column].isna() * 100)
        print(column, ": ", round(missing, 1), "%")


# Третье задание шестой практической работы
def task3():
    print('\n\nВыполнение третьего задания:\n')

    print(data[['day', 'month', 'year']].describe())
    print()
    print(data[['cases', 'deaths', 'popData2019']].describe())

    data_death_3000 = data[data['deaths'] > 3000]
    print()
    print(data_death_3000)

    print('\nСтраны со смертностью выше 3000: ',
          data_death_3000['countriesAndTerritories'].unique())
    print('Количество дней со смертностью выше 3000: ',
          len(data_death_3000['dateRep'].unique()))


# Четвертое задание шестой практической работы
def task4():
    print('\n\nВыполнение четвертого задания:\n\n'
          'Статистика строк по дубликатам до фильтрации:')
    print(data.duplicated())

    print('\nСодержимое датасета после удаления дубликатов:')
    print(data.drop_duplicates())


# Пятое задание шестой практической работы
def task5():
    print('\n\nВыполнение пятого задания:\n')
    data5 = pd.read_csv('bmi.csv', sep=',')

    data_northwest = data5[data5['region'] == 'northwest']
    data_southwest = data5[data5['region'] == 'southwest']

    print('Выборка по северо-западу:')
    print(data_northwest)
    print('\nВыборка по юго-западу')
    print(data_southwest)

    print('\nПроверка выборки по северо-западному региону на нормальность:',
          sts.shapiro(data_northwest['bmi']))
    print('Проверка выборки по юго-западному региону на нормальность:',
          sts.shapiro(data_southwest['bmi']))
    print('\nПроверка выборок по обоим регионам на гомогенность:',
          sts.bartlett(data_northwest['bmi'], data_southwest['bmi']))

    t_res = sts.ttest_ind(data_northwest['bmi'], data_southwest['bmi'])
    print('\nРезультат сравнения средних значений'
          ' выборок по t-критерию Стьюдента:', t_res)


# Шестое задание шестой практической работы
def task6():
    print('\n\nВыполнение шестого задания:\n')
    data6 = pd.DataFrame([[1, 97, 100],
                          [2, 98, 100],
                          [3, 109, 100],
                          [4, 95, 100],
                          [5, 97, 100],
                          [6, 104, 100]],
                         columns=['Point', 'Observed', 'Expected'])
    print(data6.to_string(index=False))
    stat, p = sts.chisquare(data6['Observed'], data6['Expected'])
    print('\nРезультат проверки критерия Хи-квадрат: p-значение =', p)


# Седьмое задание шестой практической работы
def task7():
    print('\n\nВыполнение седьмого задания:\n')
    data7 = pd.DataFrame({'Женат': [89, 17, 11, 43, 22, 1],
                          'Гражданский брак': [80, 22, 20, 35, 6, 4],
                          'Не состоит в отношениях': [35, 44, 35, 6, 8, 22]
                          })
    data7.index = ['Полный рабочий день',
                   'Частичная занятость',
                   'Временно не работает',
                   'На домохозяйстве',
                   'На пенсии',
                   'Учёба']
    print(data7)
    chi, p, dof, ex = sts.chi2_contingency(data7)
    print('\nРезультат проверки критерия Хи-квадрат: p-значение =',
          format(p, '.30f'))


task1()
task2()
task3()
task4()
task5()
task6()
task7()
