import pandas
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import time
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier


# Датасет для работы в практической работе
# предобработка не требуется - дубликатов нет изначально
data = pandas.read_csv('diabetes.csv', sep=',')


def task1():
    print('\nВыполнение первого задания:\n'
          'Процент нечисловых значений в датасете:')
    for column in data.columns:
        missing = np.mean(data[column].isna() * 100)
        print(column, ": ", round(missing, 1), "%", sep='')

    print('\nПервые 5 строк датасета:\n', data.head())


def task2():
    data.hist()
    plt.tight_layout()
    plt.show()
    # data.shape
    print('\nВыполнение второго задания:\n'
          'Кол-во людей без диабета и с ним:\n',
          data["Outcome"].value_counts(), sep='')


# Разбиение выборки на тренировочную и тестовую для 3-5 заданий
x = data.drop(["Outcome"], axis=1)
y = data["Outcome"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=88)


def task3():
    print('\nВыполнение третьего задания:\n'
          'Размерность набора данных x_train: ', x_train.shape,
          '\nРазмерность набора данных x_test: ', x_test.shape,
          '\nРазмерность набора данных y_train: ', y_train.shape,
          '\nРазмерность набора данных y_test: ', y_test.shape)


# Вспомогательная функция построения графической матрицы ошибок
def plot_confusion_matrix(data_confusion, title='Матрица ошибок', cmap=plt.cm.bone):
    plt.matshow(data_confusion, cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(data_confusion.columns))
    plt.xticks(tick_marks, data_confusion.columns)
    plt.yticks(tick_marks, data_confusion.index)
    plt.xlabel(data_confusion.columns.name)
    plt.ylabel(data_confusion.index.name)
    plt.show()


def task4and5():
    print('\nВыполнение четвертого и пятого заданий:\n'
          'Применение метода логистической регрессии:\n')
    start = time.perf_counter()

    # Вычисление логистической регрессии
    logisticReg = LogisticRegression()
    logisticReg.fit(x_train, y_train.ravel())
    prediction = logisticReg.predict(x_test)
    print(classification_report(y_test, prediction))

    elapsed = time.perf_counter() - start

    print('Время выполнения:', round(elapsed, 3),
          'сек\nКоэффициент точности (accuracy score):',
          round(accuracy_score(y_test, prediction) * 100),
          '%\nЧисловое представление матрицы ошибок:\n',
          confusion_matrix(y_test, prediction))

    data_confusion = pandas.crosstab(y_test, prediction)
    plot_confusion_matrix(data_confusion)

    print('\nПрименение метода SVM (метод опорных векторов):\n')
    start = time.perf_counter()

    # Применение метода SVM
    model = svm.SVC(kernel='linear', C=1.0)
    model.fit(x_train, y_train)
    svm_predict = model.predict(x_test)
    print(classification_report(y_test, svm_predict))

    elapsed = time.perf_counter() - start

    print('Время выполнения:', round(elapsed, 3),
          'сек\nКоэффициент точности (accuracy score):',
          round(accuracy_score(y_test, svm_predict) * 100),
          '%\nЧисловое представление матрицы ошибок:\n',
          confusion_matrix(y_test, svm_predict))

    data_confusion = pandas.crosstab(y_test, svm_predict)
    plot_confusion_matrix(data_confusion)

    print('\nПрименение метода KNN (кол-во ближайших соседей):\n')
    start = time.perf_counter()

    knn_model = KNeighborsClassifier(n_neighbors=25)
    knn_model.fit(x_train, y_train)
    knn_predict = knn_model.predict(x_test)
    print(classification_report(y_test, knn_predict))

    elapsed = time.perf_counter() - start

    print('Время выполнения:', round(elapsed, 3),
          'сек\nКоэффициент точности (accuracy score):',
          round(accuracy_score(y_test, knn_predict) * 100),
          '%\nЧисловое представление матрицы ошибок:\n',
          confusion_matrix(y_test, knn_predict))

    data_confusion = pandas.crosstab(y_test, knn_predict)
    plot_confusion_matrix(data_confusion)


task1()
task2()
task3()
task4and5()
