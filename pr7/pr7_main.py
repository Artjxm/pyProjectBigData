import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
import math

# Переменные для первой и второй задач
var1 = np.array([80, 98, 75, 91, 78])
var2 = np.array([100, 82, 105, 89, 102])


# Подсчет корреляции между переменными "Улица" и "Гараж" по Пирсону
def task1():
    print('Выполнение первого задания:\n'
          'Корреляция по Пирсону: ', np.corrcoef(var1, var2)[0, 1])


# Построение диаграммы рассеяния для первого задания
def task2():
    plt.grid(True)
    plt.title('Диаграмма рассеяния', fontsize=20)
    plt.xlabel('Машин на улице')
    plt.ylabel('Машин в гараже')
    plt.scatter(var1, var2, marker='o', color='orange')
    plt.show()


# Датасет для 3-11 задач
data = pd.read_csv('bitcoin.csv', sep=',', index_col=0)


# Вывод в консоль скачанного датасета bitcoin.csv
def task3():
    print('\nВыполнение третьего задания:\n'
          'Датасет bitcoin.csv\n', data)


# Удаление последних 14 дней из датасета
data = data.drop(labels=[1987, 1988, 1989, 1990, 1991, 1992, 1993,
                          1994, 1995, 1996, 1997, 1998, 1999, 2000],
                  axis=0)


# Вывод датасета без 14 последних дней
def task4():
    print('\nВыполнение четвертого задания:\n'
          'Датасет bitcoin.csv без 14 последних дней\n', data)


# Выполнение 5-11 заданий
def task5to11():
    print('\nВыполнение 5-11 заданий:\n')
    projection = 14
    data['predict'] = data['close'].shift(-projection)

    # Цена закрытия, признак, который мы подаем на вход модели
    x = pd.DataFrame(data, columns=['close'])

    # Данные, которые мы хотим получить на выход
    y = pd.DataFrame(data, columns=['predict'])

    # Нормализация для нормального среза (я плоховато это понимаю, тавтология)
    x = np.array(x, type(float))
    y = np.array(y, type(float))

    x = x[:-projection]
    y = y[:-projection]

    model = LinearRegression()
    model.fit(x, y)

    plt.figure(figsize=(6, 6))
    plt.grid(True)
    plt.scatter(x, y, alpha=0.3)

    plt.plot(x, model.predict(x), color='orange', linewidth=2)
    plt.xlabel('Цена закрытия $')
    plt.ylabel('Спрогнозированная цена $')
    plt.show()

    print('Угловой коэффициент линии регрессии: ', model.coef_)

    print('Угол наклона линии регрессии: ', math.degrees(math.atan(model.coef_)))

    print('Y-перехват: ', model.intercept_)

    fourteen_days_prediction = model.predict(
        np.array(pd.DataFrame(data, columns=['close']))[-projection:])
    print('\nПрогноз стоимости криптовалюты за последние 14 дней:\n',
          fourteen_days_prediction)

    print('\nТочность прогнозируемой цены закрытия: ', model.score(x, y))

    fourteen_close = np.array(data[['close']][-projection:])
    print('\nСкрытые значения стоимости криптовалюты: \n', fourteen_close)

    print('\nРазличие между скрытыми и прогнозируемыми значениями: ',
          np.max(np.absolute(fourteen_close - fourteen_days_prediction)))


# Датасет для 12-16 задач
data2 = pd.read_csv('housePrice.csv')


# Вывод датасета до предобработки
def task12():
    print('\nВыполнение 12 задания:\n'
          'Датасет housePrice.csv до предобработки\n', data2)


# Выполнение заданий 13-16
def task13to16():
    print('\nВыполнение 13 задания:',
          '\nСведения по пропускам до фильтрации:\n', data2.isna().sum())

    data2['Address'] = data2['Address'].fillna('other')
    print('\nСведения по пропускам после фильтрации:\n', data2.isna().sum())

    # Предобработка датасета
    fixed_data = data2.drop_duplicates()
    print('\nДатасет housePrice.csv после предобработки\n', fixed_data)

    # Очистка датасета от новых пустых значений и приведение к числовому виду
    cond = fixed_data['Area'].apply(lambda a: len(a) <= 3)
    data = fixed_data.where(cond).dropna()
    data['Area'] = pd.to_numeric(data['Area'])

    x = data['Area']
    y = data['Price(USD)']
    lin_reg_result = assisting_func_for_task14(x, y)
    print('\nВыполнение 14 задания:\n'
          'Результаты вычисления линейной регрессии вручную: ',
          lin_reg_result)

    # Вывод угла наклона и у-перехвата
    print('\nВыполнение 15 задания:\n'
          'Угол наклона: ', math.degrees(math.atan(lin_reg_result[1])),
          '\nY-перехват: ', lin_reg_result[0])

    # Визуализация линии регрессии на диаграмме рассеивания
    plt.figure(figsize=(6, 6))
    plt.grid(True)
    plt.scatter(x, y, alpha=0.3)

    y_pred = lin_reg_result[0] + lin_reg_result[1] * x

    plt.plot(x, y_pred, color='orange', linewidth=2)
    plt.xlabel('Площадь')
    plt.ylabel('Цена (USD)')
    plt.show()


def assisting_func_for_task14(x, y):
    # Количество точек
    n = np.size(x)

    # Среднее арифметическое параметров
    m_x = np.mean(x)
    m_y = np.mean(y)

    # Вычисление поперечного отклонения и X-отклонения
    cross_deviation = np.sum(y * x) - n * m_y * m_x
    x_deviation = np.sum(x * x) - n * m_x * m_x

    # Вычисление коэффициентов регрессии
    var1 = cross_deviation / x_deviation
    var2 = m_y - var1 * m_x
    return var2, var1


task1()
task2()
task3()
task4()
task5to11()
task12()
task13to16()
