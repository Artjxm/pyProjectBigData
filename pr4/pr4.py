import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
import scipy.stats as sts
import pandas as pd
import seaborn as sns

path = "insurance.csv"
insurance_data = pd.read_csv(path, sep=',')


# Второе задание четвертой практической работы
# использование метода describe()
def task2():
    print('Результат выполнения второго задания:\n\n',
          insurance_data.describe()), '\n'


# Третье задание - вывод гистограммы
def task3():
    insurance_data.hist()
    plt.show()
    print('\nРезультат выполнения третьего задания представлен на гистограммах')


# Четвертое задание - поиск мер центральной тенденции,
# мер изменчивости для индекса массы тела и расходов,
# а также вывод в консоль и на вертикальные графики
def task4():
    bmi_data = insurance_data["bmi"]
    charges_data = insurance_data["charges"]
    bmi = []
    charges = []

    for i in range(len(bmi_data)):
        bmi.append(bmi_data[i])
    for j in range(len(charges_data)):
        charges.append(charges_data[j])

    bmi_mean = np.mean(bmi)
    bmi_mode = sts.mode(bmi)
    bmi_median = np.median(bmi)

    charges_mean = np.mean(charges)
    charges_mode = sts.mode(charges)
    charges_median = np.median(charges)

    print('\nРезультат выполнения четвертого задания:\n\n',
          'Мера центральной тенденции для индекса массы тела\n',
          'Среднее =', bmi_mean, '\n',
          'Мода =', bmi_mode, '\n',
          'Медиана =', bmi_median, '\n\n',
          'Мера центральной тенденции для расходов\n',
          'Среднее =', charges_mean, '\n',
          'Мода =', charges_mode, '\n',
          'Медиана =', charges_median, '\n\n')

    bmi_std = bmi_data.std()
    bmi_diff = bmi_data.max() - bmi_data.min()

    bmi_1quarter = np.percentile(bmi_data, 25, method='midpoint')
    bmi_3quarter = np.percentile(bmi_data, 75, method='midpoint')
    bmi_midquartal = bmi_3quarter - bmi_1quarter

    charges_std = charges_data.std()
    charges_diff = charges_data.max() - charges_data.min()

    charges_1quarter = np.percentile(charges_data, 25, method='midpoint')
    charges_3quarter = np.percentile(charges_data, 75, method='midpoint')
    charges_midquartal = charges_3quarter - charges_1quarter

    print('Мера изменчивости для индекса массы тела\n'
          'Стандартное отклонение:', bmi_std, '\n',
          'Размах:', bmi_diff, '\n',
          'Межквартальные размах:', bmi_midquartal, '\n\n',
          'Мера изменчивости для расходов\n',
          'Стандартное отклонение:', charges_std, '\n',
          'Размах:', charges_diff, '\n',
          'Межквартальный размах:', charges_midquartal)

    fig, ax = plt.subplots(1, 2, figsize=(16, 8))
    plt.suptitle('Четвертое задание')

    ax[0].hist(insurance_data["bmi"], edgecolor='k', color='g', bins=15, label='bmi')
    ax[0].vlines(bmi_mode.mode, ymin=0, ymax=200, color='b', label='Мера центральной тенденции (мода)')
    ax[0].vlines(bmi_mean, ymin=0, ymax=200, color='r', label='Мера центральной тенденции (среднее)')
    ax[0].vlines(bmi_median, ymin=0, ymax=200, color='y', label='Мера центральной тенденции (медиана)')
    ax[0].vlines(bmi_std, ymin=0, ymax=200, color='orange', label='Мера изменчивости (стандартное отклонение)')
    ax[0].vlines(bmi_diff, ymin=0, ymax=200, color='m', label='Мера изменчивости (размах)')
    ax[0].vlines(bmi_midquartal, ymin=0, ymax=200, color='c', label='Мера изменчивости (межквартальный размах)')
    ax[0].legend()

    ax[1].hist(insurance_data["charges"], edgecolor='k', color='g', bins=15, label='charges')
    ax[1].vlines(charges_mode.mode, ymin=0, ymax=400, color='b', label='Мера центральной тенденции (мода)')
    ax[1].vlines(charges_mean, ymin=0, ymax=400, color='r', label='Мера центральной тенденции (среднее)')
    ax[1].vlines(charges_median, ymin=0, ymax=400, color='y', label='Мера центральной тенденции (медиана)')
    ax[1].vlines(charges_std, ymin=0, ymax=400, color='orange', label='Мера изменчивости (стандартное отклонение)')
    ax[1].vlines(charges_diff, ymin=0, ymax=400, color='m', label='Мера изменчивости (размах)')
    ax[1].vlines(bmi_midquartal, ymin=0, ymax=400, color='c', label='Мера изменчивости (межквартальный размах)')
    ax[1].legend()

    plt.show()


# Пятое задание - box-plot диаграммы числовых показателей с легендой
def task5():
    fig, axes = plt.subplots(2, 2, sharex='all', figsize=(8, 8))
    fig.suptitle('Пятое задание')

    sns.boxplot(ax=axes[0, 0], data=insurance_data["age"]).set_title('Возраст')
    sns.boxplot(ax=axes[0, 1], data=insurance_data["bmi"]).set_title('Индекс массы тела')
    sns.boxplot(ax=axes[1, 0], data=insurance_data["children"]).set_title('Кол-во детей')
    sns.boxplot(ax=axes[1, 1], data=insurance_data["charges"]).set_title('Расходы')
    plt.show()

    print('\nРезультат выполнения пятого задания представлен на диаграммах')


# Шестое задание - выполнение проверки центральной предельной теоремы
# путем замеров различных длин выборок, результат затем выводится в виде
# гистограмм с отклонениями (стандартным и средним)
def task6():
    task6_1()
    task6_2()
    task6_3()
    print('Результат выполнения шестого задания представлен на диаграммах')


def task6_1():
    bmi_arr = []

    for i in range(300):
        bmi_data = insurance_data["bmi"].sample(n=10)
        mean = np.mean(bmi_data)
        bmi_arr.append(mean)

    sns.distplot(bmi_arr)
    plt.vlines(np.mean(bmi_arr), 0, 0.18, color='k', lw=3, label="Среднее отклонение")
    plt.vlines(np.mean(bmi_arr) + np.std(bmi_arr), 0, 0.18, color='r', lw=3, label="Стандартное отклонение")
    plt.vlines(np.mean(bmi_arr) - np.std(bmi_arr), 0, 0.18, color='r', lw=3)
    plt.legend()
    plt.title('Первая длина выборок')

    plt.show()


def task6_2():
    bmi_arr = []

    for j in range(300):
        bmi_data = insurance_data["bmi"].sample(n=100)
        mean = np.mean(bmi_data)
        bmi_arr.append(mean)

    sns.distplot(bmi_arr)
    plt.vlines(np.mean(bmi_arr), 0, 0.6, color='k', lw=3, label="Среднее отклонение")
    plt.vlines(np.mean(bmi_arr) + np.std(bmi_arr), 0, 0.6, color='r', lw=3, label="Стандартное отклонение")
    plt.vlines(np.mean(bmi_arr) - np.std(bmi_arr), 0, 0.6, color='r', lw=3)
    plt.legend()
    plt.title('Вторая длина выборок')

    plt.show()


def task6_3():
    bmi_arr = []

    for j in range(300):
        bmi_data = insurance_data["bmi"].sample(n=1000)
        mean = np.mean(bmi_data)
        bmi_arr.append(mean)

    sns.distplot(bmi_arr)
    plt.vlines(np.mean(bmi_arr), 0, 4.5, color='k', lw=3, label="Среднее отклонение")
    plt.vlines(np.mean(bmi_arr) + np.std(bmi_arr), 0, 4.5, color='r', lw=3, label="Стандартное отклонение")
    plt.vlines(np.mean(bmi_arr) - np.std(bmi_arr), 0, 4.5, color='r', lw=3)
    plt.legend()
    plt.title('Третья длина выборок')
    plt.show()


# Седьмое задание - построение 95- и 99-процентных доверительных
# интервалов для средних значений расходов и индекса массы тела
def task7():
    bmi_data = insurance_data['bmi']
    charges_data = insurance_data['charges']
    print('\nРезультат выполнения седьмого задания:\n\n',
          '95% доверительный интервал для среднего значения индекса массы тела\n',
          sts.t.interval(0.95,
                         df=bmi_data,
                         loc=np.mean(bmi_data),
                         scale=sts.sem(bmi_data),
                         ),
          '\n\n99% доверительный интервал для среднего значения индекса массы тела\n',
          sts.t.interval(0.99,
                         df=bmi_data,
                         loc=np.mean(bmi_data),
                         scale=sts.sem(bmi_data),
                         ),
          '\n\n95% доверительный интервал для среднего значения расходов\n',
          sts.t.interval(0.95,
                         df=charges_data,
                         loc=np.mean(charges_data),
                         scale=sts.sem(charges_data),
                         ),
          '\n\n99% доверительный интервал для среднего значения расходов\n',
          sts.t.interval(0.99,
                         df=charges_data,
                         loc=np.mean(charges_data),
                         scale=sts.sem(charges_data),
                         )
          )


# def taskExtra():
#     bmi_arr = bmi_arr2 = bmi_arr3 = []
#
#     for i in range(300):
#         bmi_data = insurance_data["bmi"].sample(n=10)
#         mean = np.mean(bmi_data)
#         bmi_arr.append(mean)
#
#     for j in range(300):
#         bmi_data = insurance_data["bmi"].sample(n=100)
#         mean = np.mean(bmi_data)
#         bmi_arr2.append(mean)
#
#     for k in range(300):
#         bmi_data = insurance_data["bmi"].sample(n=1000)
#         mean = np.mean(bmi_data)
#         bmi_arr3.append(mean)
#
#     plt.suptitle('Шестое задание')
#     plt.figure(figsize=(21, 7))
#     vlineheight = 1.5
#     plt.subplot(1, 3, 1)
#     sns.distplot(bmi_arr)
#     plt.vlines(np.mean(bmi_arr), 0, 1.2, color='k', lw=3, label="Среднее отклонение")
#     plt.vlines(np.mean(bmi_arr) + np.std(bmi_arr), 0, vlineheight, color='r', lw=3, label="Стандартное отклонение")
#     plt.vlines(np.mean(bmi_arr) - np.std(bmi_arr), 0, vlineheight, color='r', lw=3)
#     plt.legend()
#     plt.title('Первая длина выборок')
#
#     plt.subplot(1, 3, 2)
#     sns.distplot(bmi_arr2)
#     vlineheight2 = 1.5
#     plt.vlines(np.mean(bmi_arr2), 0, vlineheight2, color='k', lw=3, label="Среднее отклонение")
#     plt.vlines(np.mean(bmi_arr2) + np.std(bmi_arr2), 0, vlineheight2, color='r', lw=3, label="Стандартное отклонение")
#     plt.vlines(np.mean(bmi_arr2) - np.std(bmi_arr2), 0, vlineheight2, color='r', lw=3)
#     plt.legend()
#     plt.title('Вторая длина выборок')
#
#     plt.subplot(1, 3, 3)
#     sns.distplot(bmi_arr3)
#     vlineheight3 = 1.5
#     plt.vlines(np.mean(bmi_arr3), 0, vlineheight3, color='k', lw=3, label="Среднее отклонение")
#     plt.vlines(np.mean(bmi_arr3) + np.std(bmi_arr3), 0, vlineheight3, color='r', lw=3, label="Стандартное отклонение")
#     plt.vlines(np.mean(bmi_arr3) - np.std(bmi_arr3), 0, vlineheight3, color='r', lw=3)
#     plt.legend()
#     plt.title('Третья длина выборок')
#
#     plt.show()

print('')

task2()
task3()
task4()
task5()
task6()
task7()
# taskExtra()
