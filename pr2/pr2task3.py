# Третья программа второй практической работы
# был использован пакет numpy, из которого понадобились
# функции numpy.random.rand() для заполнения матрицы и
# matrix.flatten() для уплощения матрицы по желаемому формату
import numpy as np

rowAmount = int(input('Введите кол-во строк матрицы: '))
columnAmount = int(input('Введите кол-во столбцов матрицы: '))
print(rowAmount, columnAmount)
myMatrix = np.random.rand(rowAmount, columnAmount)
myMatrix.flatten()
print('Полученный вектор:', *myMatrix)
