import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.arcsin(np.sqrt(x / (1+x)))  # функция описывающая подинтегральное выражение

def trapez_rule(f, a, b, n):  # метод трапеций
    h = (b - a) / n  # шаг
    x = np.linspace(a, b, n+1)  # массив значений x
    y = f(x)  # массив значений y
    integral = h * (0.5*y[0] + np.sum(y[1:-1]) + 0.5*y[-1])  # вычисляем интеграл
    return integral  # возвращаем значение интеграла

def adaptive_trapez(f,a,b,e):
    n = 1  # начально число подинтервалов
    integral = trapez_rule(f, a, b, n)  # вычисляем интеграл
    while True:  # эмулируем цикл do-while
        n *= 2  # увеличиваем количество разбиений вдвое
        integral_new = trapez_rule(f, a, b, n)  # вычисляем новый интеграл
        if abs(integral_new - integral) < e:  # если разница между новым и старым интегралом меньше точности
            return integral_new  # возвращаем новый интеграл
        integral = integral_new  # если разница больше - обновляем старый интеграл

def rectangle_rule(f, a, b, n):  # метод прямоугольников
    h = (b - a) / n  # шаг
    x = np.linspace(a, b, n+1)  # массив значений x
    y = f(x)  # массив значений y
    integral = h * np.sum(y[:-1])  # вычисляем интеграл
    return integral  # возвращаем значение интеграла

def adaptive_rectangle(f, a, b, e):  # адаптивный метод прямоугольников
    n = 1  # начально число подинтервалов
    integral = rectangle_rule(f, a, b, n)  # вычисляем интеграл
    while True:  # эмулируем цикл do-while
        n *= 2  # увеличиваем количество разбиений вдвое
        integral_new = rectangle_rule(f, a, b, n)  # вычисляем новый интеграл
        if abs(integral_new - integral) < e:  # если разница между новым и старым интегралом меньше точности
            return integral_new  # возвращаем новый интеграл
        integral = integral_new  # если разница больше - обновляем старый интеграл

def simpson_rule(f, a, b, n):  # метод Симпсона
    h = (b - a) / n  # шаг
    x = np.linspace(a, b, n+1)  # массив значений x
    y = f(x)  # массив значений y
    integral = h / 3 * (y[0] + 2*np.sum(y[2:-1:2]) + 4*np.sum(y[1:-1:2]) + y[-1])  # вычисляем интеграл
    return integral  # возвращаем значение интеграла

def adaptive_simpson(f, a, b, e):  # адаптивный метод Симпсона
    n = 2  # начальное число подинтервалов
    integral = simpson_rule(f, a, b, n)  # вычисляем интеграл
    while True:  # эмулируем цикл do-while
        n *= 2  # увеличиваем количество разбиений вдвое
        integral_new = simpson_rule(f, a, b, n)  # вычисляем новый интеграл
        if abs(integral_new - integral) < e:  # если разница между новым и старым интегралом меньше точности
            return integral_new  # возвращаем новый интеграл
        integral = integral_new  # если разница больше - обновляем старый интеграл

def bld():  # строим график функции
    x = np.linspace(0, 3, 1000)  # массив значений x
    y = f(x)  # массив значений y
    x1 = np.linspace(0, 3.5, 1000)
    x2 = np.linspace(0, 1.5, 1000)
    y1 = x*0

    plt.plot(x, y, '--r')  # строим график
    plt.plot(x1,y1,'k')  # строим вспомогательную ось
    plt.plot(y1,x2, 'k')  # строим вспомогательную ось
    
    plt.xlabel('x', fontsize = 16)  # подписываем оси
    plt.ylabel('y', fontsize = 16)
    plt.title("f(x) = arcsin(sqrt(x / (1+x)))")  # заголовок
  
    plt.minorticks_on()  # включаем отображение дополнительных отсечек сетки
    plt.grid(which = 'major')  # включаем основную сетку
    plt.grid(which = 'minor', linestyle = ':')  # включаем дополнительную сетку
    plt.fill_between(x, y, y1, where = (x >= 0) & (x <= 3), color = 'blue', alpha = 0.5)  # закрашиваем область под графиком

    plt.tight_layout()  # включаем автоматическое красивое отображение
    return plt.show()

if __name__ == "__main__":  # точка входа
    a = 0  # нижний предел интегрирования
    b = 3  # верхний предел интегрирования
    e = 1e-4  # точность

    res1 = trapez_rule(f, a, b, 1000)  # вычисляем интеграл методом трапеций
    res2 = adaptive_trapez(f, a, b, e)  # вычисляем интеграл методом адаптивных трапеций
    res3 = rectangle_rule(f, a, b, 1000)  # вычисляем интеграл методом прямоугольников
    res4 = adaptive_rectangle(f, a, b, e)  # вычисляем интеграл методом адаптивных прямоугольников
    res5 = simpson_rule(f, a, b, 1000)  # вычисляем интеграл методом Симпсона
    res6 = adaptive_simpson(f, a, b, e)  # вычисляем интеграл адаптивным методом Симпсона

    print("Метод трапеций: ", res1)
    print("Адаптивный метод трапеций: ", res2)
    print("Метод прямоугольников: ", res3)
    print("Адаптивный метод прямоугольников: ", res4)
    print("Метод Симпсона: ", res5)
    print("Адаптивный метод Симпсона: ", res6)

    bld()  # строим график функции