from __future__ import division
from random import randint
import matplotlib.pyplot as plt
from collections import Counter
import math
import numpy as np


numbers = np.random.randint(1, 100, 100)
print(f"numbers: {numbers}")
count = Counter(numbers)
# print(count)
xs = range(101)
ys = [count[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histogram of Count ")
plt.xlabel("# numbers")
plt.ylabel("# count")
plt.show()

num_points = len(numbers)
largest_value = max(numbers)
smallest_value = min(numbers)
sorted_value = sorted(numbers)


print(f'largest_value: {largest_value}')
print(f"smallest_value: {smallest_value}")
print(f"sorted_value: {sorted_value}")

# Central Tendencies


def mean(x):
    return sum(x) / len(x)


print(f"mean: {mean(numbers)}")


def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2
    if n % 2 == 1:
        return sorted_v[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2


print(f"median: {median(numbers)}")


def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]


print(f"quantile = 0,10: {quantile(numbers, 0.10)}")
print(f"quantile = 0,25: {quantile(numbers, 0.25)}")
print(f"quantile = 0,75: {quantile(numbers, 0.75)}")
print(f"quantile = 0,90: {quantile(numbers, 0.90)}")


def mode(x):
    counter = Counter(x)
    max_count = max(count.values())
    return [x_i for x_i, counter in counter.items() if counter == max_count]


print(f"mode: {mode(numbers)}")


# Dispersion

def data_range(x):
    return max(x) - min(x)


print(f"data range: {data_range(numbers)}")


def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


print(f"de_mean: {de_mean(numbers)}")
print(f"max de_mean: {max(de_mean(numbers))}")
print(f"min de_mean: {min(de_mean(numbers))}")

# """ assumes x has at least two elements """


def sum_of_squares(x):
    return sum([x_i ** x_i for x_i in x])


print(f"sum of squares: {sum_of_squares(numbers)}")


def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)


print(f"variance: {variance(numbers)}")


def standard_deviation(x):
    return math.sqrt(variance(x))


print(f"standard_deviation: {standard_deviation(numbers)}")


def quartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)


print(f"quartile_range: {quartile_range(numbers)}")




