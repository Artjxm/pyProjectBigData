# В этой программе мы используем формулу Герона для подсчета площади треугольника
# а также используем структуру словарь для вывода результата вычислений
import cmath


def triangle(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area


def rectangle(a, b):
    return a * b


def circle(r):
    return cmath.pi * r * r


dictionary = {
    'треугольник':
        triangle(int(input('первая сторона треугольника: ')),
                 int(input('вторая сторона треугольника: ')),
                 int(input('третья сторона треугольника: '))),
    'прямоугольник':
        rectangle(int(input('первая сторона прямоугольника: ')),
                  int(input('вторая сторона прямоугольника: '))),
    'круг': circle(int(input('радиус круга: ')))}

print(dictionary)
