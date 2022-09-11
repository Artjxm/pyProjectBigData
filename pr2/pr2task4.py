# Четвертая программа второй практической работы
# использовались базовые структуры данных
# (список и словарь), цикл for, а также метод sorted()
# для упорядочивания словаря по ключам
listA = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2]
listB = ['a', 'b', 'c', 'c', 'c', 'b', 'a', 'c',
         'a', 'a', 'b', 'c', 'b', 'a']
myDict = {}

for i in set(listB):
    myDict[i] = 0

for i in myDict:
    counter = 0
    for j in range(len(listB)):
        if i == listB[j]:
            counter += listA[j]
    myDict[i] = counter

print('Результат работы программы:', dict(sorted(myDict.items())))
