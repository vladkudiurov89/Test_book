import numpy as np

date = [-6, 0, 1, 2, 4, 5, 5, 6, 7, 100]


def get_median(arr):
    return np.median(arr)


def get_a(arr):
    return arr[:len(arr)//2]


def get_b(arr):
    return arr[len(arr)//2:]


def get_interval(arr):
    a = get_median(get_a(date))
    b = get_median(get_b(date))
    z = b - a
    return a - 1.5 * z, b + 1.5 * z


def get_ejection(arr):
    for i in arr:
        if i in get_interval(arr):
            print('IS NOT EJECTION')
        else:
            print('IS EJECTION')


# print(get_median(date))
print(get_median(get_a(date)))
print(get_median(get_b(date)))
print(get_interval(date))
print(get_ejection(date))


def get_interval_1():
    a = 2
    b = 4
    z = b - a
    return a - 1.5 * z, b + 1.5 * z

print(get_interval_1())