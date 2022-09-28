import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.express as px

# Второе задание практической работы
# В данной программе в терминале выводится информация
# о данных при помощи .info() и .head()
#
# также Пятое задание практической работы
# Строится линейный график с накопленными значениями
# количественного показателя от даты
#
# также Седьмое задание практической работы
# Графики создаются при помощи библиотеки matplotlib

path = 'C:\\House_Rent_Dataset.csv'


def secondAndFifth():
    df = pd.read_csv(path, sep=',', index_col=0)

    # Выполнение второго задания
    print(df.head())
    print(df.info())

    # Выполнение пятого задания
    # Переменные для вывода на график значений из базы данных
    a = df['Size']
    b = df['Rent']

    # Для удобства вывода установим семь выводимых значений
    # Возможно установить любое число
    df = df[:7]

    # Параметры диалогового окна
    fgr = plt.figure('Задание пять', figsize=(10, 6))

    # Задание 5.3
    # Установка сетки у графика
    plt.grid(True, color='azure')

    # Заголовок графика
    plt.title('График цен на дома', fontsize=20)

    # Обозначение осей X и Y
    plt.xlabel('t, дата', fontsize=12)
    plt.ylabel('$, цена', fontsize=12)

    # Параметры осей X и Y
    plt.xticks(np.arange(start=0, stop=len(df), step=1), rotation=17, size=10, )
    plt.yticks(size=10)

    # Задание 5.1
    # Параметры оформления графика
    plt.plot(
        df['Rent'],
        # Метка
        marker='.',
        # Размер метки линейной функции
        markersize=3,
        # Цвет меток
        markerfacecolor='darkblue',
        # Цвет контура меток
        markeredgecolor='black',
        # Цвет линейной функции
        color='crimson',
        # Толщина линии линейной функции
        linewidth=2
    )

    # Задание 5.2
    # Установка легенды графика
    plt.legend(
        # Расположение легенды
        loc='lower left',
        # Цвет области
        facecolor='oldlace',
        # Цвет обводки
        edgecolor='r',
        # заголовок
        title='7 домов',
        # размер шрифта заголовка
        title_fontsize='15'
    )
    plt.show()


def three():
    df = pd.read_csv(path, sep=',', index_col=0)
    a = df['Size']
    b = df['Rent']

    # Для удобства вывода установим десять выводимых значений
    # Возможно установить любое число
    df = df[:10]
    a = a[:10]
    b = b[:10]

    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    # первая диаграмма
    ax[1].bar(a, b, color='teal', edgecolor='blue')
    ax[1].grid(alpha=0.3, zorder=1)
    ax[1].set_title('Диаграмма')
    ax[1].set_ylabel('TWh')
    # вторая диаграмма
    ax[0].barh(a, b, color='teal',
               edgecolor="black")
    ax[0].grid(alpha=0.3, zorder=1)
    ax[0].set_title('Диаграмма')
    ax[0].set_ylabel('Twh')
    plt.show()


def three():
    df = pd.read_csv(path, sep=',', index_col=0)
    a = df['Size']
    b = df['Rent']
    name = ['blue', 'red', 'green', 'black', 'orange', 'grey', 'purple', 'brown', 'pink', 'yellow']
    # Для удобства вывода установим десять выводимых значений
    # Возможно установить любое число
    df = df[:10]
    a = a[:10]
    b = b[:10]
    fig = go.Figure(px.bar(x=a, y=b, color=name, text=b))
    fig.update_traces(textfont_size=14, textangle=0, textposition="outside",
                      marker=dict(line=dict(color='black', width=2)))
    fig.update_layout(
        title='Дома', title_font_size=20, title_xanchor='left', title_pad_l=700,
        xaxis_title='X', xaxis_title_font_size=20, xaxis_tickfont_size=20,
        yaxis_title='Y', yaxis_titlefont_size=18, yaxis_tickfont_size=16, legend_y=-0.1,
        margin=dict(l=50, r=0, t=30, b=0)
    )
    # legend_y=-0.1 укорачивает Y координату на 10%
    fig.show()


def four():
    df = pd.read_csv(path, sep=',', index_col=0)
    a = df['Size']
    b = df['Rent']
    df = df[:50]
    a = a[:20]
    b = b[:10]
    fig = go.Figure()
    # Отображаемые параметры на всей странице
    fig.update_traces(textfont_size=14, textangle=0, textposition="outside",
                      marker=dict(line=dict(color='black', width=2)))
    fig.add_trace(go.Pie(values=a, labels=a.index))
    fig.update_layout(
        title='Дома', title_font_size=20, title_xanchor='left', title_pad_l=650,
        margin=dict(l=50, r=0, t=30, b=0)
    )
    fig.show()


# Выполнение шестого задания
def six():
    df = pd.read_csv(path, sep=',', index_col=0)
    a = df['Size']
    b = df['Rent']
    df = df[:10]
    # a=a[:10]
    b = b[:20]
    # c=a[10:20]
    plt.boxplot(b)
    plt.grid(True, color='azure')
    plt.xlabel('Rent', fontsize=12)
    plt.legend(loc='lower left',
               facecolor='oldlace',
               edgecolor='r',
               title='10 домов',
               title_fontsize='15')
    plt.show()


secondAndFifth()
three()
three()
four()
six()
