import math
from functools import reduce, partial


# сложение элементов векторов
def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]


# разность элементов векторов
def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]


v = [3, 8]
w = [2, 7]
a = vector_add(v, w)
b = vector_subtract(v, w)
print("vector v: ", v)
print('vector w :', w)
print(f'vector add: {a}')
print(f'vector subtract: {b}')


# покомпонентная сумма списка векторов
def vector_sum(vectors):
    result = vectors[0]
    for _ in vectors[1:]:
        result = vector_add(result, _)
    return result


vectors = [v, w]
print(f'vectors sum: {vector_sum(vectors)}')


def vector_sum_1(vectors):
    return reduce(vector_add, vectors)


print(f"vector sum 1: {vector_sum_1(vectors)}")

vector_sum_2 = partial(reduce, vector_add)
print(vector_sum_2)


# умножение вектора на скаляр
def scalar_multiply(c, v):
    return [c * v_i for v_i in v]


c = 9
print(f'scalar multiply c = 9, v = [3, 8]: {scalar_multiply(c, v)}')


# среднее значение списка векторов
def vector_mean(c, v):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))


print(f'vector mean c = 9, v = [3, 8]: {vector_mean(c, v)}')


# скалярное произведение вектора
def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


print(f'dot: {dot(v, w)}')


def sum_of_squares(v):
    return dot(v, v)


print(f'sum of squares v: {sum_of_squares(v)}')
print(f'sum of squares w: {sum_of_squares(w)}')


# вычисление величины
def magnitude(v):
    return math.sqrt(sum_of_squares(v))


print(f'magnitude v: {magnitude(v)}')
print(f'magnitude w: {magnitude(w)}')


# квадрат расстояния между двумя векторами
def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))


print(f'squared distance between vectors v and w: {squared_distance(v, w)}')


# расстояние между двумя векторами
def distance(v, w):
    return math.sqrt(squared_distance(v, w))


print(f'distance between vectors v and w: {distance(v, w)}')


def distance(v, w):
    return magnitude(vector_subtract(v, w))


print(f'distance:{distance(v, w)}')


