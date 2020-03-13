import numpy as np


def find_min(arr):
    min_arr = arr[0]
    index_min_arr = 0
    for el in range(1, len(arr)):
        if arr[el] < min_arr:
            min_arr = arr[el]
            index_min_arr = el
    return index_min_arr


def fast_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        small_el = find_min(arr)
        new_arr.append(arr.pop(small_el))
    return new_arr


if __name__ =='__main__':
    date_list = list(np.random.randint(1, 55, 40, dtype=int))
    print(date_list)
    print(fast_sort(date_list))
