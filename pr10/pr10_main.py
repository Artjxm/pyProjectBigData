import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import plotly.graph_objects as go
from sklearn.metrics import silhouette_score
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
import time

# Датасет для работы берется из прошлой работы
data = pd.read_csv('../pr9/diabetes.csv', sep=',')


# Переменные для замера времени работы алгоритмов
delta1 = delta2 = delta3 = 0


def task1():
    print('\nВыполнение первого задания:\n'
          'Процент нечисловых значений в датасете:')
    for column in data.columns:
        missing = np.mean(data[column].isna() * 100)
        print(column, ":", round(missing, 1), "%")

    print('\nПервые 5 строк датасета:\n', data.head())


def task2():
    print('\nВыполнение второго задания:\n'
          'Результат кластеризации представлен на диаграммах.')

    models = []
    score1 = []
    score2 = []

    for i in range(2, 10):
        model = KMeans(n_clusters=i, random_state=88, init='k-means++').fit(data)
        models.append(model)
        score1.append(model.inertia_)
        score2.append(silhouette_score(data, model.labels_))

    plt.grid()
    plt.plot(np.arange(2, 10), score1, marker='o')
    plt.show()
    plt.grid()
    plt.plot(np.arange(2, 10), score2, marker='o')
    plt.show()

    start = time.perf_counter()

    model1 = KMeans(n_clusters=2, random_state=88, init='k-means++')
    model1.fit(data)

    global delta1
    delta1 = time.perf_counter() - start

    print('\nКоординаты центров кластеров:\n',
          model1.cluster_centers_)

    labels = model1.labels_
    data['Cluster'] = labels

    print('\nОптимальное кол-во кластеров при k-means кластеризации:\n',
          data['Cluster'].value_counts(), sep='')

    fig = go.Figure(data=[go.Scatter3d(x=data['Age'],
                                       y=data['Outcome'],
                                       z=data['DiabetesPedigreeFunction'],
                                       mode='markers',
                                       marker_color=data['Cluster'],
                                       marker_size=4)])
    fig.show()


def task3():
    print('\nВыполнение третьего задания:\n'
          'Результат иерархической кластеризации данных'
          ' представлен на трехмерной диаграмме.')

    start = time.perf_counter()

    model2 = AgglomerativeClustering(2, compute_distances=True)
    clustering = model2.fit(data)

    global delta2
    delta2 = time.perf_counter() - start

    data['Cluster'] = clustering.labels_
    print('\nОптимальное кол-во кластеров при иерархической кластеризации:\n',
          data['Cluster'].value_counts(), sep='')

    fig = go.Figure(data=[go.Scatter3d(x=data['Age'],
                                       y=data['Outcome'],
                                       z=data['DiabetesPedigreeFunction'],
                                       mode='markers',
                                       marker_color=data['Cluster'],
                                       marker_size=4)])
    fig.show()


def task4():
    print('\nВыполнение четвертого задания:\n'
          'Результат кластеризации данных с помощью алгоритма'
          ' DBSCAN представлен на трехмерной диаграмме.')

    start = time.perf_counter()

    model3 = DBSCAN(eps=11, min_samples=5).fit(data)
    data['Cluster'] = model3.labels_

    global delta3
    delta3 = time.perf_counter() - start

    print('\nОптимальное кол-во кластеров при '
          'кластеризации алгоритмом DBSCAN:\n',
          data['Cluster'].value_counts(), sep='')

    fig = go.Figure(
        data=[go.Scatter3d(x=data['Age'],
                           y=data['Outcome'],
                           z=data['DiabetesPedigreeFunction'],
                           mode='markers',
                           marker_color=data['Cluster'],
                           marker_size=4)])
    fig.show()


def task5():
    print('\nВыполнение пятого задания:\n'
          'Результат сравнения быстродействия алгоритмов '
          'представлен на следующей таблице:',
          "\nНазвание алгоритма                   | Время работы\n"
          "----------------------------------------------------------",
          "\nАлгоритм k-means                     |", round(delta1, 6),
          "сек\n----------------------------------------------------------",
          "\nАлгоритм иерархической кластеризации |", round(delta2, 6),
          "сек\n----------------------------------------------------------",
          "\nАлгоритм DBSCAN                      |", round(delta3, 6), 'сек')


task1()
task2()
task3()
task4()
task5()
