import pandas
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.ensemble import BaggingClassifier
from xgboost import XGBClassifier
import time

# Датасет для работы берется из прошлой работы
data = pandas.read_csv('../pr9/diabetes.csv', sep=',')


def task1():
    print('\nВыполнение первого задания:\n\n'
          'Процент нечисловых значений в датасете:')
    for column in data.columns:
        missing = np.mean(data[column].isna() * 100)
        print(column, ":", round(missing, 1), "%")


# Разбиение выборки на тренировочную и тестовую для 2-3 заданий
X = data.drop(['Outcome'], axis=1)
Y = data['Outcome']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)


def task2():
    print('\n\nВыполнение второго задания:\n')

    start = time.perf_counter()

    baggingCl = BaggingClassifier(n_estimators=10, max_samples=0.7, bootstrap=True)
    baggingCl = baggingCl.fit(X_train, Y_train)
    test_predict = baggingCl.predict(X_test)
    baggingCl_score = baggingCl.score(X_test, Y_test)

    delta = time.perf_counter() - start
    print('Время работы баггинга:', round(delta, 6), 'сек')

    print("Точность баггинг модели равна: {} %".format(round((baggingCl_score * 100), 6)))
    print("\nМатрица ошибок баггинг модели следующая:")
    print(metrics.confusion_matrix(Y_test, test_predict))

    y_predict = baggingCl.predict_proba(X_test)
    # print('Предсказанные данные:\n', y_predict)

    auc = metrics.roc_auc_score(Y_test, y_predict[:, 1])
    print('Точность обучения (AUC) баггингом = {} %'.format(round((auc * 100), 6)))


def task3():
    print('\n\nВыполнение третьего задания:\n')

    start = time.perf_counter()

    xgbCl = XGBClassifier()
    xgbCl.fit(X_train, Y_train)
    test_predict = xgbCl.predict(X_test)
    xgbCl_score = xgbCl.score(X_test, Y_test)

    delta = time.perf_counter() - start
    print('Время работы алгоритма XGBoost:', round(delta, 6), 'сек')

    print("Точность XGBoostClassifier модели равна: {} %".format(round((xgbCl_score * 100), 6)))
    print("\nМатрица ошибок XGBoostClassifier модели следующая:")
    print(metrics.confusion_matrix(Y_test, test_predict))

    y_predict = xgbCl.predict_proba(X_test)
    # print('Предсказанные данные:\n', y_predict)

    auc = metrics.roc_auc_score(Y_test, y_predict[:, 1])
    print('Точность обучения (AUC) алгоритмом XGBoost = {} %'.format(round((auc * 100), 6)))


task1()
task2()
task3()
