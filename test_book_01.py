import random
import re
from functools import partial, reduce

# Функции-генераторы и генераторы выражения


def lazy_range(n):
    i = 0
    while i < n:
        yield i
        i += 1
    print(i)


a = lazy_range(25)
print(a)

# бесконечные числа


def natural_numbers(n=1):
    while True:
        yield n
        n += 1
        print(natural_numbers(25))


# ленивый список четных чисел меньше 49

lazy_evens_below_49 = (i for i in lazy_range(49) if i % 2 == 0)
print(f'lazy evens below 49: {lazy_evens_below_49}')

# Случайные числа
# import random
# Случайные величины
uniform_randoms = [random.random() for _ in range(5)]
print(f'uniform randoms: {uniform_randoms}')

# Когда требуется получить воспроизводимые результаты, внутреннее состояние
# можно задать при помощи метода random.seed()
random.seed(50)
print(f'random random 50: {random.random()}')
random.seed(500)
print(f'random random 500: {random.random()}')

# random.randrange - принимает один или два аргумента и возвращает элемент ,
# выбранный случайно из соответствующей последовательности range():
print(f'random randrange 50: {random.randrange(50)}')
print(f'random randrange 250~500: {random.randrange(250, 500)}')

# Метод random.shuffle - перемешивает элементы в списке в случайном порядке
ten = range(10, 1)
print(ten)
random.shuffle(ten)
print(f'ten:{ten}')

# Лотерейные номера
lottery_numbers = range(600)
print(f'lottery numbers: {lottery_numbers}')
print(f'lottery numbers 600: {lottery_numbers}')

# Случайное имя
my_best_friend = random.choice(['John', "Bob", 'Charlie'])
print(f'my best friend: {my_best_friend}')

# Список из элементов(пример выборки с возвратом)
with_replacement = [random.choice(range(2000)) for _ in range(20)]
print(f'with replacement: {with_replacement}')

# Регулярные выражения - предостовляют средства для поиска в тексте
# import re

print(all([not re.match('a', 'cat'), re.search('a', 'cat'), not re.search('c', 'dog'),
            3 == len(re.split('[ab]', 'carbs')), "R-D" == re.sub("[0-9]", "-", "R2d2")]))

# Объектно - ориентированное программирование


class Set:
    def __init__(self, values=None):
        # s1 = Set()
        # s2 = Set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.dict = {}
        if values is not None:
            for value in values:
                self.add(value)

    def __repr__(self):
        return "Set: " + str(self.dict.keys())

    def add(self, value):
        self.dict[value] = True

    def contains(self, value):
        return value in self.dict

    def remove(self, value):
        del self.dict[value]


s = Set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(f'Set S: {s}')
s.add(10)
print(f's.contains(10): {s.contains(10)}')
s.remove(10)
print(f'Set S: {s.contains(10)}')

# Инструменты функционального программирования


def exp(x, y):
    return x ** y


a = exp(2, 2)
print(f'x^y: {a}')


def power_two(power):
    return exp(2, power)


b = power_two(9)
print(f'x^9: {b}')

# Использование функции partial
# from functools import partial
two_power = partial(exp, 2)
print(f'two power: {two_power(3)}')


def double(x):
    return x * 2


xs = [1, 2, 3, 4, 5]
twice_xs = [double(x) for x in xs]
print(f'twice xs:{twice_xs}')
twice_xs_map = list(map(double, xs))
print(f'twice xs with map: {twice_xs_map}')
list_doubler = partial(map, double)
print(f'list doubler: {list_doubler}')
twice_xs = list_doubler(xs)
print(f'twice xs: {twice_xs}')

# Функцию map используют с функциями нескольких аргументов,предоставляя ей несколько списков
# переумножить аргументы


def multiply(x, y):
    return x * y


product = list(map(multiply, [1, 2], [4, 5]))
print(f'product: {product}')

mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
kilometer_distances = list(map(lambda x: x * 1.6, mile_distances))
print(f'kilometres distances: {kilometer_distances}')
# Функция filter работает аналогично генератору последовательности с условием if


def is_even(x):
    return x % 2 == 0


xs = [random.choice(range(200)) for _ in range(20)]
print(f'xs: {xs}')
x_evens = [x for x in xs if is_even(x)]
print(f'x evens: {x_evens}')
y_evens = list(filter(is_even, xs))
print(f'y evens: {y_evens}')
list_evener = partial(filter, is_even)
print(f'list evener: {list_evener}')

# Функция reduce выполняет свертку списка,т.е. объединяет первые два элемента, затем этот результат
# с третьим элементом, а тот с четвертым и т.д., возвращая единственный результат
# from functools import reduce

x_product = reduce(multiply, xs)
print(f'x product: {x_product}')
list_product = partial(reduce, multiply)
print(f'list product:{list_product}')
x_product = list_product(xs)
print(f'x product: {x_product}')

# Функция enumerate итеративно обходит список, используя как элементы,
# так и их индексы

# for i, j in enumerate(xs): print(i, xs)
# for i, j in enumerate(xs): print(j)

# Функция zip и распаковка аргументов
# zip преобразует несколько списков в один список кортежей,
# состоящий из соответствующих элементов

list_1 = ['a', 'b', 'c']
list_2 = [1, 2, 3]
new_list = list(zip(list_1, list_2))
print(f'new list: {new_list}')

# * выполняет распаковку аргументов, которая использует элементы пар
# в качестве индивидуальных аргументов
new_list = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*new_list)
print(f'letters: {list(letters)}')
print(f'numbers: {list(numbers)}')

# Переменные args и kwargs


def magic(*args, **kwargs):
    print(f'Безымянные аргументы: {args}')
    print(f'Аргументы по ключу: {kwargs}')


magic(1, 2, key='word', key2="word2")

# args - кортеж из безымянных позиционных аргументов
# kwargs - словарь из именнованных аргументов


def other_way_magic(x, y, z):
    return x + y + z


x_y_list = [1, 2]
z_dict = {"z": 3}
print(f"sum items: {other_way_magic(*x_y_list, **z_dict)}")


def doubler(f):
    def g(x):
        return 2 * f(x)
    return g


def f1(x):
    return x + 1


g = doubler(f1)
print(g(3))
print(g(-1))


def f2(x, y):
    return x + y


def double_correct(f):
    def g(*args, **kwargs):
        return 2 * f(*args, **kwargs)
    return g


g = double_correct(f2)
print(g(1, 2))