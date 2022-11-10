import pandas
import scipy.stats as sts
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt


# Отключение предупреждений в консоли
pandas.options.mode.chained_assignment = None  # default='warn'

# Основной датасет без дублированных значений
data = pandas.read_csv('insurance.csv', sep=',')
data = data.drop_duplicates()

# Предобработка вспомогательных датасетов для
# второго и четвертого заданий
data_bmi = data[['bmi', 'region']]
southwest = data_bmi[data_bmi['region'] == 'southwest']
southwest.drop('region', axis=1, inplace=True)
southeast = data_bmi[data_bmi['region'] == 'southeast']
southeast.drop('region', axis=1, inplace=True)
northwest = data_bmi[data_bmi['region'] == 'northwest']
northwest.drop('region', axis=1, inplace=True)
northeast = data_bmi[data_bmi['region'] == 'northeast']
northeast.drop('region', axis=1, inplace=True)


def task1():
    print('Выполнение первого задания:\n'
          'Уникальные регионы:', data['region'].unique())


def task2():
    print('\nВыполнение второго задания:\n'
          'Однофакторный ANOVA тест через Scipy:\n',
          sts.f_oneway(southwest, southeast, northwest, northeast))


def task3():
    model = ols('bmi ~ region', data=data_bmi).fit()
    anova_result = sm.stats.anova_lm(model, typ=2)
    print('\nВыполнение третьего задания:\n'
          'Однофакторный ANOVA тест через anova_lm() из statsmodels:\n',
          anova_result)


def task4():
    print('\nВыполнение четвертого задания:\n'
          'Перебор всех пар с помощью t критерия Стьюдента:')
    regions = ["southwest", "southeast", "northwest", "northeast"]
    region_pairs = []

    for region1 in range(3):
        for region2 in range(region1 + 1, 4):
            region_pairs.append((regions[region1], regions[region2]))

    for region1, region2 in region_pairs:
        print('Пара ', region1, ' и ',  region2, ':', sep='')

        if region1 == 'southwest':
            if region2 == 'southeast':
                print(sts.ttest_ind(southwest, southeast))
            elif region2 == 'northwest':
                print(sts.ttest_ind(southwest, northwest))
            elif region2 == 'northeast':
                print(sts.ttest_ind(southwest, northeast))
        elif region1 == 'southeast':
            if region2 == 'southwest':
                print(sts.ttest_ind(southeast, southwest))
            elif region2 == 'northwest':
                print(sts.ttest_ind(southeast, northwest))
            elif region2 == 'northeast':
                print(sts.ttest_ind(southeast, northeast))
        elif region1 == 'northwest':
            if region2 == 'southeast':
                print(sts.ttest_ind(northwest, southeast))
            elif region2 == 'southwest':
                print(sts.ttest_ind(northwest, southwest))
            elif region2 == 'northeast':
                print(sts.ttest_ind(northwest, northeast))
        elif region1 == 'northeast':
            if region2 == 'southeast':
                print(sts.ttest_ind(northeast, southeast))
            elif region2 == 'northwest':
                print(sts.ttest_ind(northeast, northwest))
            elif region2 == 'southwest':
                print(sts.ttest_ind(northeast, southwest))


def task5():
    tukey = pairwise_tukeyhsd(endog=data_bmi['bmi'], groups=data_bmi['region'], alpha=0.05)
    tukey.plot_simultaneous()
    plt.vlines(x=30.66, ymin=-0.5, ymax=4.5, color='orange')
    print('\nВыполнение пятого задания:\n'
          'Пост-хок тесты Тьюки:\n', tukey.summary())
    plt.show()


# Вспомогательный датасет для шестого и седьмого заданий
data_bmi_for_6_and_7 = data[['bmi', 'region', 'sex']]


def task6():
    model = ols('bmi ~ region + sex + region:sex', data=data_bmi_for_6_and_7).fit()
    anova_result = sm.stats.anova_lm(model, typ=2)
    print('\nВыполнение шестого задания:\n'
          'Двухфакторный ANOVA тест влияния региона'
          ' и пола на BMI через anova_lm():\n', anova_result)


def task7():
    data_bmi_for_6_and_7['combination'] = data_bmi_for_6_and_7.region \
                                          + '/' \
                                          + data_bmi_for_6_and_7.sex
    tukey = pairwise_tukeyhsd(endog=data_bmi_for_6_and_7['bmi'],
                              groups=data_bmi_for_6_and_7['combination'],
                              alpha=0.05)
    tukey.plot_simultaneous()
    plt.vlines(x=30.66, ymin=-0.5, ymax=7.5, color='blue')
    plt.show()
    print('\nВыполнение седьмого задания:\n'
          'Пост-хок тесты Тьюки:\n', tukey.summary())


task1()
task2()
task3()
task4()
task5()
task6()
task7()


