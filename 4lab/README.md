## Лабораторная работа №4

## Задание 1
Замыкание для генерации последовательности Фибоначчи. Я создала замыкание fibonacci_closure, которое устанавливает начальные значения a = 0 и b = 1. Внутренняя функция fibonacci возвращает текущее значение a и обновляет a и b для следующего вызова. Замыкание возвращает функцию fibonacci, которая запоминает значения a и b между вызовами.
## Результаты вычислений
![alt text](image-1.png)
## Задание 2
Декоратор для кэширования результатов функций. Создала декоратор cache_decorator, который принимает функцию func.Внутри декоратора создается словарь cache для хранения результатов вызовов функции. Функция wrapper проверяет, есть ли результат для данных аргументов в кэше. Если есть, возвращает его, иначе вызывает исходную функцию func, сохраняет результат в кэше и возвращает его.Декоратор возвращает функцию wrapper, которая заменяет исходную функцию func.
## Результаты вычислений
![alt text](image-2.png)
## Задание 3
Объединение замыкания и декоратора для генерации Фибоначчи с кэшированием. Создала замыкание fib, которое возвращает функцию fibonacci с кэшированием. В цикле вызываю fib() 10 раз, и каждое число Фибоначчи выводится в одной строке через пробел.
## Результат вычислений
![alt text](image-3.png)
## Список использованных источников:
1. [Замыкание](https://habr.com/ru/articles/862692/)
2. [Декоратор](https://proglib.io/p/keshirovanie-v-python-algoritm-lru-2020-11-17)
