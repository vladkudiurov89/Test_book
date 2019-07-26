Кудюров В.

1. Оценить асимптотическую сложность приведенного ниже алгоритма:
a = len(arr) - 1
out = list()
while a > 0:
    out.append(arr[a])
    a = a // 1.7
out.merge_sort()
print('O * (log_1.7 (N) * log_2 Log_1.7 (N))')

2. Считалочка
Дано N человек, считалка из K слогов. Считалка начинает считать с первого человека.
Когда считалка досчитывает до k-го слога, человек, на котором она остановилась, вылетает.
Игра происходит до тех пор, пока не останется последний человек.
Для данных N и К дать номер последнего оставшегося человека.


people = 13
words = 21

new_list = [i for i in range(1, people+1)]
print(new_list)
finish = False
counter = 0
first_out = 0
while not finish:
    if len(new_list) == 1:
        finish = True
        print(f'Winner: {new_list[0]}')
    else:
        if words > people:
            del_people = words - people - 1 + first_out
            if del_people >= len(new_list):
                while del_people >= len(new_list):
                    del_people = del_people - len(new_list)
        else:
            del_people = words - 1 + first_out
            while len(new_list) <= del_people:
                del_people = del_people - len(new_list)
        del new_list[del_people]
        first_out = del_people
        if first_out > len(new_list):
            first_out = first_out - len(new_list) - 1
        print(new_list)


3. Назовем связным такой граф, в котором есть путь от любой вершины к любой другой вершине.
Дан граф, состоящий из 2+ связных подграфов, которые не связаны между собой.
Задача: посчитать число компонент связности графа, т.е. количество таких подграфов.
В графе на картинке – три подграфа, т.е. число компонент связности = 3.


4. Навигатор на сетке.
Дана плоская квадратная двумерная сетка (массив),
на которой определена стоимость захода в каждую ячейку (все стоимости положительные).
Необходимо найти путь минимальной стоимости из заданной ячейки в заданную ячейку и вывести этот путь.


net = [[19, 11, 43, 16],
       [32, 21, 17, 15],
       [33, 18, 9, 27],
       [48, 1,  39, 41]]


def navigator(x, y):
    net_new = []
    for i in range(x,y):
        for j in range(len(net[i])):
            net_min = min(net[i])
            net_1 = net[i].index(net_min)
            net_2 = net[i][:net_1:]
            net_new.append(net_2)
            break

    print(net_new)

navigator(1, 4)


5. Задача консенсуса DNA ридов
При чтении DNA последовательностей могут возникать единичные ошибки, выражающиеся в неверной букве в строке.
Для решения данной проблемы требуемое место читается несколько раз, после чего строится консенсус-строка,
в которой на каждом месте будет стоять тот символ, что чаще всего встречался в этом месте суммарно во всех чтениях.
Т.е. для строк
ATTA
ACTA
AGCA
ACAA
консенсус-строка будет ACTA (в первой ячейке чаще всего встречалась A,
во второй – C, в третьей – Т, в четвертой – снова А).
Для входного списка из N строк одинаковой длины построить консенсус-строку.

import collections

word = [['A', 'T', 'T', 'A'],
        ['A', 'C', 'T', 'A'],
        ['A', 'G', 'C', 'A'],
        ['A', 'C', 'A', 'A']]


def row(word):
    word_1 = []
    word_2 = []
    v = {}
    s = ''
    for w in range(len(word_1)):
        word_2.append(word[w][word])
        v = collections.Counter(word_2)
    for i,j in iter(v.items()):
        if j == max(v.values()):
            s = i
    return s
row(word)


6. Аренда ракет
Вы – компания, дающая в аренду ракеты. Каждый день к вам приходит список заявок на использование ракет в виде:
(час_начала, час_конца), (час_начала, час_конца), ...
Если аренда ракеты заканчивается в час X, то в этот же час ее уже можно взять в аренду снова
(т.е. час_начала может начинаться с Х).
Дано: список заявок на использование ракет
Задача: вывести ответ, хватит ли вам одной ракеты, чтобы удовлетворить все заявки на этот день

list_order = [(4, 3), (7, 9), (8, 2), (6, 2)]
new_list = []

def rent_rocket(list_order, new_list):
    rocket = True
    for first_rocket in list_order:
        start_time = first_rocket[0]
        finish_time = first_rocket[1]
        time = range(start_time, finish_time)
        for second_rocket in list_order:
            if first_rocket == second_rocket or second_rocket in new_list:
                pass
            else:
                if second_rocket[0] == start_time:
                    rocket = False
                if second_rocket[1] in time:
                    rocket = False
                if second_rocket[0] in time:
                    rocket = False
                if start_time in range(second_rocket[0], second_rocket[1] + 1):
                    rocket = False
        new_list.append(first_rocket)


    if rocket:
        print('Enough first rocket')
    else:
        print('Do not enough first rocket')


rent_rocket(list_order,new_list)


