import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def f1(x):  # первая функция
    return 2*x**4 + 8*x**3 + 8*x**2 - 1

def df1(x):  # производная первой функции
    return 8*x**3 + 24*x**2 + 16*x

def f2(x):  # приведённый вид второй функции
    return np.cos(x) - 1/(x-3)

def df2(x):  # производная второй функции
    return -np.sin(x) + 1/(x-3)**2

def fibonacci_search(f, a, b, epsilon):
  # Вычисляем число итераций
  k = 0
  while (b - a) > epsilon:
    k += 1

  # Вычисляем числа Фибоначчи
  fib_minus_2 = 0
  fib_minus_1 = 1
  fib_k = fib_minus_1 + fib_minus_2

  while fib_k < (b - a) / epsilon:
    fib_minus_2 = fib_minus_1
    fib_minus_1 = fib_k
    fib_k = fib_minus_1 + fib_minus_2

  # Инициализация точек
  x1 = b - fib_minus_1 / fib_k * (b - a)
  x2 = a + fib_minus_1 / fib_k * (b - a)

  while fib_k > 1:
    if f(x1) > f(x2):
      b = x2
      x2 = x1
      fib_k = fib_minus_2
      fib_minus_2 = fib_minus_1 - fib_minus_2
      x1 = b - fib_minus_1 / fib_k * (b - a)
    else:
      a = x1
      x1 = x2
      fib_k = fib_minus_2
      fib_minus_2 = fib_minus_1 - fib_minus_2
      x2 = a + fib_minus_1 / fib_k * (b - a)

  return (a + b) / 2

def gradient_descent(f, df, x0, learning_rate, max_iter):
    x = x0
    for _ in range(max_iter):
        x -= learning_rate * df(x)
    return x

def bld1(xmax,ymax):  # строим график первой функции
    x = np.linspace(-2.8, 0.8, 1000)
    y = f1(x)  # массив значений y
    x1 = np.linspace(-3, 1, 1000)
    x2 = np.linspace(-2, 9.5, 1000)
    y1 = x*0

    plt.plot(x, y, '--r')  # строим график
    plt.plot(x1,y1,'k')  # строим вспомогательную ось
    plt.plot(y1,x2, 'k')  # строим вспомогательную ось
    plt.plot(xmax, ymax, 'bo')  # строим точку максимума
    plt.plot(0, f1(0), 'co')  # строим точку миниммума
    plt.plot(-2, f1(-2), 'co')  # строим точку минимума
    
    plt.xlabel('x', fontsize = 16)  # подписываем оси
    plt.ylabel('y', fontsize = 16)
    plt.title("f(x) = 2*x^4 + 8*x^3 + 8*x^2 - 1")  # заголовок
  
    plt.minorticks_on()  # включаем отображение дополнительных отсечек сетки
    plt.grid(which = 'major')  # включаем основную сетку
    plt.grid(which = 'minor', linestyle = ':')  # включаем дополнительную сетку

    plt.tight_layout()  # включаем автоматическое красивое отображение
    return plt.show()

def bld2(xmax,ymax):  # строим график второй функции
    x = np.linspace(-4.5, 2.5, 1000)
    y = f2(x)  # массив значений y
    x1 = np.linspace(-5, 3, 1000)
    x2 = np.linspace(-2, 4, 1000)
    y1 = x*0

    plt.plot(x, y, '--r')  # строим график
    plt.plot(x1,y1,'k')  # строим вспомогательную ось
    plt.plot(y1,x2, 'k')  # строим вспомогательную ось
    plt.plot(xmax, ymax, 'bo')  # строим точку максимума
    plt.plot(-3.174,-0.837,'bo')  # строим точку минимума

    
    plt.xlabel('x', fontsize = 16)  # подписываем оси
    plt.ylabel('y', fontsize = 16)
    plt.title("f(x) = cos(x) - 1/(x-3)")  # заголовок
  
    plt.minorticks_on()  # включаем отображение дополнительных отсечек сетки
    plt.grid(which = 'major')  # включаем основную сетку
    plt.grid(which = 'minor', linestyle = ':')  # включаем дополнительную сетку

    plt.tight_layout()  # включаем автоматическое красивое отображение
    return plt.show()

if __name__ == "__main__":  # точка входа
    # быдлокод ON
    roots1 = [-2.0, -1.0, 0.0]  # прикинули корешки продифференцированной функции на глазок
    # быдлокод OFF

    print(roots1)
    # Проверяем, какие из найденных точек являются максимумами
    for root1 in roots1:
        if df1(root1 - 0.001) > 0 and df1(root1 + 0.001) < 0:  # Проверка знака второй производной
            print(f"Локальный максимум первой функции в точке x = {root1:.4f}, y = {f1(root1):.4f}")
            x1 = root1
    
    roots2 = fsolve(df2, [-4, 0, 2])  # Начальные приближения для поиска корней
    # Проверяем, какие из найденных точек являются максимумами
    for root2 in roots2:
        if df2(root2 - 0.001) > 0 and df2(root2 + 0.001) < 0:  # Проверка знака второй производной
            print(f"Локальный максимум второй функции в точке x = {root2:.4f}, y = {f2(root2):.4f}")
            x2 = root2

    a1 = -3  # Левая граница отрезка 
    b1 = 1   # Правая граница отрезка
    eps = 0.001  # Точность

    a2 = 2  # Левая граница отрезка для второй функции
    b2 = 4  # Правая граница отрезка для второй функции
    
    #x_max1 = fibonacci_search(f1, a1, b1, eps)  # Максимум первой функции
    #x_max2 = fibonacci_search(f2, a2, b2, eps)  # Максимум второй функции

    #print("Максимум первой функции через фибоначчи:", x_max1, f1(x_max1))
    #print("Максимум второй функции через фибоначчи:", x_max2, f2(x_max2))

    # Для функции f(x) = 2x^4 + 8x^3 + 8x^2 - 1
    x01 = -2  # Начальное приближение
    learning_rate1 = 0.01  # Скорость обучения
    max_iter1 = 1000  # Максимальное число итераций

    result1 = gradient_descent(f1, df1, x01, learning_rate1, max_iter1)
    print("Минимум первой функции достигается в точке x =", result1)

    # Для функции f(x) = cos(x) + 1 / (x - 3)
    x02 = 2  # Начальное приближение
    learning_rate2 = 0.1  # Скорость обучения
    max_iter2 = 1000  # Максимальное число итераций

    result2 = gradient_descent(f2, df2, x02, learning_rate2, max_iter2)
    print("Минимум второй функции достигается в точке x =", result2)

    #bld1(x1, f1(x1))
    bld2(x2, f2(x2))