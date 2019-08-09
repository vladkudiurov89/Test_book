# Gradient Descent
import distance as distance
import matplotlib.pyplot as plt
from functools import partial
import random
import LinearAlgebra

def sum_squares(v):
    return sum(v_i ** 2 for v_i in v)


def difference_quotient(f, x, h):
    return (f(x + h) - f(x)) / h


def square(x):
    return x * x


def derivative(x):
    return 2 * x


derivative_estimate = partial(difference_quotient, square, h=0.00001)
x = range(-10, 10)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
plt.title("Actual Derivatives vs. Estimates")
plt.plot(a, "rx", label="Actual")
plt.plot(b, "b+", label="Estimate")
plt.legend(loc=9)
plt.show()


def partial_difference_quotient(f, v, i, h):
    w = [v_j + (h if j == i else 0) for j, v_j in enumerate(v)]
    return (f(w) - f(v)) / h


def estimate_gradient(f, v, h=0.00001):
    return [partial_difference_quotient(f, v, i, h) for i in enumerate(v)]


# Using the Gradient

def step(v, direction, step_size):
    return [v_i + step_size * direction_i for v_i, direction_i in zip(v, direction)]


def sum_of_squares_gradient(v):
    return [2 * v_i for v_i in v]


v = [random.randint(-10, 10) for i in range(3)]
tolerance = 0.0000001
while True:

    gradient = sum_of_squares_gradient(v)
    next_v = step(v, gradient, -0.01)
    dd = v.cdist(next_v, v)
    if distance < tolerance:
        break
    v = next_v

print(sum_of_squares_gradient(3))


# Choosing the Right Step Size


def safe(f):
    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except ValueError:
            return float("inf")
    return safe(f)


def gradient_fn(theta):
    pass


def minimize_batch(target_fn, theta_0, tolerance=0.000001):
    step_sizes = [100, 10, 1, 0.1, 0.001, 0.0001, 0.00001]
    theta = theta_0
    target_fn = safe(target_fn)
    value = target_fn(theta)
    while True:
        gradient_fn(theta)
        next_thetas = [step(theta, gradient, -step_size) for step_size in step_sizes]
        next_theta = min(next_thetas, key=target_fn)
        next_value = target_fn(next_theta)
        if abs(value - next_value) < tolerance:
            return theta
        else:
            theta, value = next_theta, next_value
            
            
def negate(f):
    return lambda *args, **kwargs: -f(*args, **kwargs)


def negate_all(f):
    return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]


def maximize_batch(target_fn, gradient_fn, theta_0):
    return minimize_batch(negate(target_fn), negate_all(gradient_fn), theta_0)


# Stochastic Gradient Descent

def in_random_order(data):
    indexes = [i for i, _ in enumerate(data)]
    random.shuffle(indexes)
    for i in indexes:
        yield data[i]


def vector_subtract(theta):
    pass


def minimize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0 = 0.01 ):
    global gradient_i
    data = zip(x, y)
    theta = theta_0
    alpha = alpha_0
    min_theta, min_value = None, float("inf")
    iterations_with_no_improvement = 0
    while iterations_with_no_improvement < 100:
        value = sum(target_fn(x_i, y_i, theta) for x_i, y_i in data)
        if value < min_value:
            min_theta, min_value = theta, value
            iterations_with_no_improvement = 0
            alpha = alpha_0
        else:
            iterations_with_no_improvement += 1
            alpha *= 0.9
        for x_i, y_i in in_random_order(data):
            gradient_i = gradient_fn(x_i, y_i, theta)
            vector_subtract(theta)
    return min_theta, gradient_i


def maximize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
    return minimize_stochastic(negate(target_fn), negate_all(gradient_fn), x, y, theta_0, alpha_0)
