import matplotlib.pyplot as plt

# test 1

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

plt.plot(xs, variance, 'g-', label='variance')
plt.plot(xs, bias_squared, 'r-.', label='bias_squared^2')
plt.plot(xs, total_error, 'b-.', label='total_error')

plt.legend(loc=9)
plt.xlabel('model complexity')
plt.title("The Bias-Variance Tradeoff")
plt.show()

# test 2

friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'j', 'h', 'i']

plt.scatter(friends, minutes)

for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
                 xy=(friend_count,minute_count),
                 xytext=(5, -5),
                 textcoords='offset points')

plt.title("Daily minutes us number of friend ")
plt.xlabel('# of friends')
plt.ylabel(' daily minutes spent on the site')
plt.show()

#  test 3

grades_1 = [99, 90, 85, 97, 80]
grades_2 = [100, 85, 60, 90, 70]

plt.scatter(grades_1, grades_2)
plt.title("Axes are not comparable")
plt.xlabel(" 1 grade")
plt.ylabel(" 2 grade")
plt.show()

# or

grades_1 = [99, 90, 85, 97, 80]
grades_2 = [100, 85, 60, 90, 70]

plt.scatter(grades_1, grades_2)
plt.axis("equal")
plt.title("Axes are not comparable")
plt.xlabel(" 1 grade")
plt.ylabel(" 2 grade")
plt.show()