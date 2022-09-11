# В этой программе была использована структура
# if/elif для создания примитивного калькулятора
def task2(a, b, c):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '/':
        return a / b
    elif c == '//':
        return a // b
    elif c == '**':
        return a ** b
    else:
        return "calculator machine broke"


print(task2(int(input('первое слагаемое: ')),
            int(input('второе слагаемое: ')),
            input('операция: ')))
