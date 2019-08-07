import math
import random


def normal_cdf(x, mu=0, sig=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sig)) / 2


def inverse_normal_cdf(p, mu=0, sig=1, tolerance=0.00001):
    if mu != 0 or sig != 1:
        return mu + sig * inverse_normal_cdf(p, tolerance=tolerance)
    low_z, how_z = -10.0, 0
    hi_z, hi_p = 10.0, 0
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p or mid_p > p:
            pass
        else:
            break
        return mid_z


def normal_approximation_to_binomial(n, p):
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma


normal_probability_below = normal_cdf


def normal_probability_above(lo, mu=0, sig=1):
    return 1 - normal_cdf(lo, mu, sig)


def normal_probability_between(lo, hi, mu=0, sig=1):
    return normal_cdf(hi, mu, sig) - normal_cdf(lo, mu, sig)


def normal_probability_outside(lo, hi, mu=0, sig=1):
    return 1 - normal_probability_between(lo, hi, mu, sig)


def normal_upper_bound(probability, mu=0, sig=1):
    return inverse_normal_cdf(probability, mu, sig)


def normal_lower_bound(probability, mu=0, sig=1):
    return inverse_normal_cdf(1 - probability, mu, sig)


def normal_two_sided_bounds(probability, mu=0, sig=1):
    tail_probability = (1 - probability) / 2
    upper_bound = normal_lower_bound(tail_probability, mu, sig)
    lower_bound = normal_upper_bound(tail_probability, mu, sig)
    return lower_bound, upper_bound


mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)
print(normal_two_sided_bounds(0.95, mu_0, sigma_0))
lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)
type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
power = 1 - type_2_probability
print("normal_approximation_to_binomial(1000, 0.5): ", power)

hi = normal_upper_bound(0.95, mu_0, sigma_0)
type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
power_1 = 1 - type_2_probability
print("normal_upper_bound(0.95, mu_0, sigma_0): ", power_1)


def two_sided_p_value(x, mu=0, sigma=1):
    if x >= mu:
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        return 2 * normal_probability_below(x, mu, sigma)


extreme_value_count = 0
for _ in range(100000):
    num_heads = sum(1 if random.random() < 0.5 else 0 for _ in range(1000))
    if num_heads >= 530 or num_heads <= 470:
        extreme_value_count += 1

upper_p_value = normal_probability_above
lower_p_value = normal_probability_below


print("normal_two_sided_bounds(0.95, mu_0, sigma_0): ", normal_two_sided_bounds(0.95, mu_0, sigma_0))
print("normal_approximation_to_binomial(1000, 0.5): ", power)
print("normal_upper_bound(0.95, mu_0, sigma_0): ", power_1)
print("two_sided_p_value(529.5, mu_0, sigma_0): ", two_sided_p_value(529.5, mu_0, sigma_0))
print("extreme_value_count / 100000: ", extreme_value_count / 100000)
print("two_sided_p_value(531.5, mu_0, sigma_0): ", two_sided_p_value(531.5, mu_0, sigma_0))
print("upper_p_value(526.5, mu_0, sigma_0): ", upper_p_value(526.5, mu_0, sigma_0))


# Confidence Intervals

p_hat = 525/1000
mu_2 = p_hat
sigma_2 = math.sqrt(p_hat * (1 - p_hat) / 1000)
print(sigma_2)
power_2 = normal_two_sided_bounds(0.95, mu_2, sigma_2)
print(power_2)

# P-hacking


def run_experiment():
    return [random.random() < 0.5 for _ in range(1000)]


def reject_fairness(experiment):
    num_heads_1 = len([flip for flip in experiment if flip])
    return num_heads_1 < 469 or num_heads_1 > 531


random.seed(1000)
experiments = [run_experiment() for _ in range(1000)]
num_rejections = len([ex for ex in experiments if reject_fairness(ex)])
print(num_rejections)

# Example: Running an A/B Test


def estimated_parameters(nn, ny):
    p = nn / ny
    sig_3 = math.sqrt(p * (1 - p) / nn)
    return p, sig_3


print(estimated_parameters(200, 1000))


def a_b_test_statistic(N_A, n_A, N_B, n_B):
    p_A, sig_A = estimated_parameters(N_A, n_A)
    p_B, sig_B = estimated_parameters(N_B, n_B)
    return (p_B - p_A) / math.sqrt(sig_A ** 2 + sig_B ** 2)


z = a_b_test_statistic(200, 1000, 180, 1000)
print(two_sided_p_value(z))

