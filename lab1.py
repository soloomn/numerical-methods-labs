import random as r
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt

def rnd(n):  # создание векторов
    list_1 = []
    for i in range(n):
        list_1.append(r.randint(-50,100))  # заполняем вспомогательный массив для создания векторов
    return list_1

def angl(v1,v2):  # вычисление угла
    scal = np.dot(v1,v2)  # скалярное произведение
    cos_angle = scal / LA.norm(v1) /LA.norm(v2)  # вычисление косинуса угла между векторами
    return cos_angle

def bld(v1,v2):  # работа с графиками
    plt.plot(v1,':b', label = '1st vector')   # работаем с функционалом pyplot - передаём массив первого вектора и делаем подпись к легенде 
    plt.plot(v2,'--r', label = '2nd vector')  # также со вторым

    plt.xlabel('x', fontsize = 16)  # подписываем оси
    plt.ylabel('vec(x)', fontsize = 16) 
    plt.legend(fontsize = 14)  # включаем отображение легенды
    
    plt.minorticks_on()  # включаем отображение дополнительных отсечек сетки
    plt.grid(which = 'major')  # включаем основную сетку
    plt.grid(which = 'minor', linestyle = ':')  # включаем дополнительную сетку

    plt.tight_layout()  # включаем автоматическое красивое отображение
    return plt.show()

def mtrx(v1,v2,n,m):  # заполнение матрицы почти случайными элементами векторов
    a = []  # главный массив
    for i in range(m):  # внешний цикл - заполняем главный массив
        b = []  # вспомогательный массив - каждый шаг внешнего цикла чистим его
        for j in range(m):  # внутренний цикл - почти случайно заполняем вспомогательный массив
            x = r.randint(0,1)  # случайно выбираем из какого вектора берём элемент
            if x == 1:  # первый вектор
                b.append(v1[r.randint(0,n-1)])  # почти случайно выбираем номер элемента в векторе
            else:  # второй вектор
                b.append(v2[r.randint(0,n-1)])  # почти случайно выбираем номер элемента в векторе
        a.append(b)  # добавляем заполненный вспомогательный массив в главный
    
    return a  # вернули массив массивов

def swap(matr, imax, jmax, imin, jmin):
    a = matr[imax][jmax]  # положительный
    b = matr[imin][jmin]  # отрицательный
    matr[imax][jmax] = b  # поменяли положительный на отрицательный
    matr[imin][jmin] = a  # поменяли отрицательный на положительный
    return matr

if __name__ == "__main__":  # точка входа
    
    print("введите количество элементов")
    n = int(input())

    vec_1 = np.array(rnd(n))  # создали первый вектор
    vec_2 = np.array(rnd(n))  # создали второй вектор

    #vec_1 = np.array([-5,-4,-3])
    #vec_2 = np.array([5,4,3])

    print("первый вектор: " + str(vec_1))
    print("второй вектор: " + str(vec_2))

    cos = angl(vec_1,vec_2)
    print("угол между векторами: " + str(np.arccos(cos)) + " радиан")

    if cos == 0 or cos == 1 or cos == -1 or np.arccos(cos) == 3.141592638688632 or np.arccos(cos) == -3.141592638688632:
        print("вектора параллельны")
    else: 
        print("вектора не параллельны")

    if LA.norm(vec_1) == LA.norm(vec_2):
        print("вектора равны по длине")
    else:
        print("вектора не равны по длине")
    
    print("-----------------------------------")
    
    print("создадим матрицу из элементов векторов")
    while True:  # эмулируем цикл do-while
        print("задайте m - размерность матрицы но так чтобы m*m <= n+n: ")
        m = int(input())
        if not (m*m > n+n):  # условие для того чтобы матрицу было возможно заполнить элементами векторов
            break
    
    matrix = np.array(mtrx(vec_1,vec_2,n,m))  # привели полученный массив массивов к виду numpy
    print("полученная матрица: ")
    print(matrix)

    min = -51  # для отрицательных - выходит за границы генерации randint()
    max = 101  # для положительных - выходит за границы генерации randint()

    for i in range(m):
        for j in range(m):
            if matrix[i][j] > 0:  # смотрим положительный элемент
                if matrix[i][j] < max:  # сравнили не меньше ли найденного 
                    max = matrix[i][j]
                    imax = i
                    jmax = j
            if matrix[i][j] < 0:  # смотрим отрицательный элемент
                if matrix[i][j] > min:  # сравниили не больше ли найденного
                    min = matrix[i][j]
                    imin = i
                    jmin = j

    flag = False

    print("-----------------------------------")

    if min == 0:
        print("отрицательных элементов нет")
        flag = True

    if max == 101:
        print("положительных элементов нет")
        flag = True

    if flag == False:
        print("минимальный положительный элемент: " + str(max))
        print("его индексы: "  + str(jmax + 1) + " " + str(imax + 1))
        print("макисмальный отрицательный элемент: " + str(min))
        print("его индексы: " + str(jmin + 1) + " " + str(imin + 1))

        print("меняем найденные элементы местами: ")
        matrix = swap(matrix, imax, jmax, imin, jmin)
        print(matrix)
    
    bld(vec_1,vec_2)  # начертили графики
