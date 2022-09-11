# Вторая программа второй практической работы
# был использован список для хранения данных
# также использовались циклы for и while
n = int(input("Введите число N, пожалуйста: "))
myList = []
for i in range(n):
    count = 0
    while count < i + 1:
        myList.append(i + 1)
        count += 1
        if n == len(myList):
            print("Результат работы программы:", *myList)
            break
