# P(B|G) = P(B,G)/P(G) = P(B)/P(G) = 1/2
# P(B|L) = P(B,L)/P(L) = P(B)/P(L) = 1/3
import random
import math
import matplotlib.pyplot as plt
from collections import Counter


def kid_random():
    return random.choice(["boy", "girl"])


girl_both = 0
girl_older = 0
girl_either = 0

random.seed(0)
for _ in range(10000):
    younger = kid_random()
    older = kid_random()
    if older == "girl":
        girl_older += 1
    if older == "girl" and younger == "girl":
        girl_both += 1
    if older == "girl" or younger == "girl":
        girl_either += 1


# print("P(both girl | older girl): ", girl_both / girl_older)
# print("P(both girl | either girl): ", girl_both / girl_either)

# Bayes's Theorem
# ds = "doesn't happen
# P(E|F) = P(E,F)/P(F) = P(F|E)P(E)/P(F)
# P(F) = P(F,E) + P(F, dsE)


def pdf(x):
    return 1 if 0 <= x <= 1 else 0


def cdf(x):
    if x < 0:
        return 0
    elif x < 1:
        return x
    else:
        return 1

# The normal Distribution


def normal_pdf(x, mu=0, sigma=1):
    pi_two_sqrt = math.sqrt(2 * math.pi)
    return math.exp(-(x - mu) ** 2 / 2 / sigma ** 2) / (pi_two_sqrt * sigma)


print(normal_pdf(2, 4, 6))

xs = [x / 10 for x in range(-50, 50)]
plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], "-", label="mu=0, sigma=1")
plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], "--", label="mu=0, sigma=2")
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ":", label="mu=0, sigma=0.5")
plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], "-.", label="mu=-1, sigma=1")
plt.legend()
plt.title("Various Normal pdfs ")
# plt.show()


def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


xz = [x / 10.0 for x in range(-50, 50)]
plt.plot(xz, [normal_cdf(x, sigma=1) for x in xz], "-", label="mu=0, sigma=1")
plt.plot(xz, [normal_cdf(x, sigma=2) for x in xz], "-", label="mu=0, sigma=2")
plt.plot(xz, [normal_cdf(x, sigma=0.5) for x in xz], "-", label="mu=0, sigma=0,5")
plt.plot(xz, [normal_cdf(x, mu=-1) for x in xz], "-", label="mu=-1, sigma=1")
plt.legend(loc=4)
plt.title("Various Normal cdfs")
plt.show()


def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    tolerance = 0.00001
    low_z, how_z = -10.0, 0
    hi_z, hi_p = 10.0, 0
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            pass
        elif mid_p > p:
            pass
        else:
            break
        return mid_z


print(inverse_normal_cdf(4, 0, 1, 0.00001))

# The Central Limit Theorem


def trial(p):
    return 1 if random.random() < p else 0


def binomial(n, p):
    return sum(trial(p) for _ in range(n))


def hist_make(p, n, numbers):
    data = [binomial(n, p) for _ in range(numbers)]
    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()], [v / numbers for v in histogram.values()], 0.8, color="0.75")
    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma) for i in xs]
    plt.plot(xs, ys)
    plt.title("Binomial Distribution vs Normal Approximation ")
    plt.show()


print(hist_make(0.75, 100, 10000))
