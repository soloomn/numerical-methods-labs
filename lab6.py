import math
import numpy as np
import matplotlib.pyplot as plt

def f1(n):  # функция 1 предел равен 1
    return 1 / ((n+2)**(1/n))

def f2(n):  # функция 2 предел равен e^3 ~ 20.0855
    return (1+(3/(n**2)))**(n**2)

def find_limit(f, epsilon=1e-2):  # функция для нахождения предела
    n = 1  # начальное значение n
    prev, curr = f(n), f(n+1)  # значения функции для n и n+1   
    st = ""  # строка для вывода

    while abs(curr - prev) > epsilon:  # пока разница больше epsilon
        prev = curr  # обновляем значения
        n += 1  # увеличиваем n
        curr = f(n+1)  # обновляем значение функции
    
    for i in range(1, n):
        a = f(i+1) - f(i)
        st = st + str(round(a,4)) + " + "
    
    st = st[:-3]
    print("частичные " + str(n) + " сумм придела до заданной точности: ")
    print(st)

    return round(curr,4)

def bld1():
    plt.subplot(2, 1, 1)
    
    x = np.linspace(1, 20, 100)
    y = f1(x)
    y1 = 1

    plt.plot(x, y, '-', label = 'приближенное значение')
    plt.title("1 / ((n+2)^(1/n))")
    plt.legend()
    plt.minorticks_on()  # включаем отображение дополнительных отсечек сетки
    plt.grid(which = 'major')  # включаем основную сетку
    plt.grid(which = 'minor', linestyle = ':')  # включаем дополнительную сетку

    plt.tight_layout()  # включаем автоматическое красивое отображение

def bld2():
    plt.subplot(2, 1, 2)
    
    x = np.linspace(1, 20, 100)
    y = f2(x)
    y1 = math.e**3

    plt.plot(x, y, '-', label = 'приближенное значение')
    plt.title("(1+(3/(n^2)))^(n^2)")
    plt.legend()
    plt.minorticks_on()  # включаем отображение дополнительных отсечек сетки
    plt.grid(which = 'major')  # включаем основную сетку
    plt.grid(which = 'minor', linestyle = ':')  # включаем дополнительную сетку

    plt.tight_layout()  # включаем автоматическое красивое отображение

if __name__ == "__main__":  # точка входа
    lim1 = find_limit(f1, 1e-2)
    print("найденное значение предела 1 функции = " + str(lim1))
    print("--------------------------------------------")

    lim2 = find_limit(f2, 1e-2)
    print("найденное значение предела 2 функции = " + str(lim2))

    bld1()
    bld2()

    plt.show()  # показываем графики