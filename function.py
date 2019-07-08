#  x = math.sqrt(x + 3) - x + 1
# f(0); f(1); f(sqrt(2)); f(sqrt(2)-1

import math

def f(x):
    return math.sqrt(x + 3) - x  + 1

# # List of values to plug in

for x in [0,1,math.sqrt(2), math.sqrt(2)-1]:
    print("f({:.3f}) = {:.3}f".format(x, f(x)))


# y = math.sqrt(y + 1) - y + 5
# fn(5); fn(sqrt(7)); fn(0); fn(sqrt(13)-10)

def fn(y):
    return math.sqrt(y + 1) - y + 5

for y in [ 0, 5, math.sqrt(7), math.sqrt(13) - 1 ]:
    print("fn({:.3f}) = {:.3}fn".format(y, fn(y)))










