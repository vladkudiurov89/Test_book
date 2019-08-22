from collections import defaultdict, Counter
import matplotlib.pyplot as plt

# Dict - структура данных, где значения связанны с ключами,
# что позволяет быстро извлекать значения, соответствующее конкретному ключу:

word_counts = {}
doc = {}
for word in doc:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Прием " Лучше просить прощения, чем разрешения "

word_counts = {}
for word in doc:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

# Метод get(), который изящно выходит из ситуации с отсутствующими ключами

word_counts = {}
for word in doc:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1

# defaultdict - словарь со значениями по умолчанию.
# from collections import defaultdict

word_counts = defaultdict(int)
for word in doc:
    word_counts[word] += 1

dd_list = defaultdict(list)
dd_list[2].append(1)
print(dd_list)

dd_dict = defaultdict(dict)
dd_dict["Joel"]["City"] = "France"
print(dd_dict)

dd_pair = defaultdict(lambda: [0, 1])
dd_pair[2][1] = 1
print(dd_pair)

# Словарь Counter - трансформирует последовательность значений похожий на словарь defaultdict(int) объект,
# где ключам поставлены в соответствии частотности или, выражаясь более точно, ключи отображаются (map) в частности,
# он  в основном применяется при создании гистограмм:
# from collections import Counter

c = Counter([0, 1, 2, 1, 0, 0])
print(c)
for word, count in c.most_common(2):
    print((word, count))

# сортировать слова в их частности по убывающему значению частот
wc = sorted(word_counts.items(), key=lambda word, count: count, reverse=True)
print(f'wc: {wc}')

# Множества set - представляет собой совокупность неупорядоченных элементов без повторов

s = set()
s.add(1)
s.add(2)
s.add(2)
s.add(3)
print(s)

x = len(s)
print(x)
y = 2 in s
print(y)
z = 6 in s
print(z)

# Список стоп-слов

item_list = [1, 2, 3, 1, 2, 3, 0]
print("item list:", item_list)
print(f"item list: {item_list}")
num_items = len(item_list)
print("num items:", num_items)
print(f'num items: {num_items}')
item_set = set(item_list)
print("item set:", item_set)
print(f"item_set: {item_set}")
num_distinct_items = len(item_set)
print("num distinct items:", num_distinct_items)
print(f"num distinct items: {num_distinct_items}")
distinct_item_list = list(item_set)
print("distance item list:", distinct_item_list)
print(f"distance item list: {distinct_item_list}")

for x in range(10):
    if x == 3:
        continue
    if x == 5:
        break
    print(x)

#  Сортировка

x = [4, 9, 3, 8, 12, 1, 5]
print(f"x: {x}")
y = sorted(x)
print(f"sorted x: {y}")
x.sort()
print(f'sort x: {x}')

# Сортировать список по абсолютному значению в убыающем порядке
a = sorted(x, key=abs, reverse=True)
print(f'reverse x: {a}')

#  Генераторы последовательностей
# четные числа
even_numbers = [x for x in range(25) if x % 2 == 0]
print(f"event numbers: {even_numbers}")

# квадраты чисел
squares = [x * x for x in range(25)]
print(f'squares: {squares}')

# квадраты в четных числах
even_squares = [x * x for x in even_numbers]
print(f'even squares: {even_squares}')

# словарь с квадратными числами
square_dict = {x: x * x for x in range(25)}
print(f'square dict: {square_dict}')

# множество с квадратными числами
square_set = {x * x for x in [11, -11]}
print(f'square set: {square_set}')

# нули
zeroes = [0 for _ in even_numbers]
print(f"zeroes: {zeroes}")

# пары
pairs = [(x, y) for x in range(25) for y in range(25)]
print(f'pairs: {pairs}')

# пары с возрастающим значением
increasing_pairs = [(x, y) for x in range(25) for y in range(x + 1, 25)]
print(f'increasing pairs: {increasing_pairs}')






