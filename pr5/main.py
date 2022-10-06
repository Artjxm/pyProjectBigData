import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from sklearn.manifold import TSNE
from umap import UMAP
import time

initial_data = pd.read_csv('fashion-mnist_test.csv', sep=',')

print(initial_data.head())

df = initial_data

scaler = preprocessing.MinMaxScaler()

df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
print(df.head())

# Функция замера и отрисовки
def sns_plot(param, title):
    draw_data = df.copy()
    draw_data['x'] = param[:, 0]
    draw_data['y'] = param[:, 1]

    fig = plt.figure()
    sns.scatterplot(data=draw_data,
                    x='x',
                    y='y',
                    hue=initial_data['label'],
                    palette='Accent')
    # plt.legend(labels=['Mammal',
    #                    'Bird',
    #                    'Reptile',
    #                    'Fish',
    #                    'Amphibian',
    #                    'Bug',
    #                    'Invertebrate'],
    #            bbox_to_anchor=(1.04, 1),
    #            borderaxespad=0)
    plt.title(label=title,
              fontsize=18,
              color='blue')
    plt.show()


def SNE_plot(perplexity: int):
    initial = time.time()
    T = TSNE(n_components=2,
             perplexity=perplexity,
             random_state=0)
    TSNE_features = T.fit_transform(df)

    final = time.time()
    diff = round(final - initial, 2)
    print('Замер времени методом TSNE: ', str(diff) + ' секунд')

    sns_plot(TSNE_features, 'Замер методом TSNE с перплекцией ' + str(perplexity))

# Запускаем первое задание на 3 значениях перплекции
print('Начались замеры для TSNE метода')
SNE_plot(5)
SNE_plot(25)
SNE_plot(99)

n_n = (5, 25, 99)
m_d = (0.1, 0.6)

print('Начались замеры для UMAP метода')

um = dict()
for i in range(len(n_n)):
    for j in range(len(m_d)):
        initial = time.time()

        local_umap = UMAP(n_neighbors=n_n[i], min_dist=m_d[j], random_state=1337)
        res = local_umap.fit_transform(df)

        final = time.time()
        diff = round(final - initial, 2)
        print('Замер времени методом UMAP:', str(diff) + ' секунд')

        um[n_n[i], m_d[j]] = res

print('Началась отрисовка методом UMAP')

for i in um.keys():
    sns_plot(um[i], 'UMAP с n_neighbors = ' + str(i[0]) + ' и min_dist = ' + str(i[1]))