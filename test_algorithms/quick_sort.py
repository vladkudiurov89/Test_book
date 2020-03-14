import numpy as np
from time import sleep


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pi_arr = arr[0]
        less = [i for i in arr[1:] if i <= pi_arr]
        great = [i for i in arr[1:] if i > pi_arr]
    return quick_sort(less) + [pi_arr] + quick_sort(great)


zz = np.random.randint(1, 50, 30, dtype=int)
print(zz)
print(quick_sort(zz))


def show_items(arr):
    for i in arr:
        print(i)


print(show_items(zz))
print(len(zz))


def show_item_2(arr):
    for i in arr:
        sleep(1)
        print(i)


print(show_item_2(zz))
print(len(zz))