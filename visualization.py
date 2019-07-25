import matplotlib.pyplot as plt
from collections import Counter

# test 1
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, gdp, color='green', marker="o", linestyle='solid')
plt.title("Nominal GDP")
plt.ylabel('Billions of $')
plt.show()


# test 2

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

xs = [i + 0.1 for i, _ in enumerate(movies)]

plt.bar(xs, num_oscars)
plt.ylabel("# of Academy Awards")
plt.title("My favorite Movies")
plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
plt.show()


# test 3

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

plt.bar([x - 4 for x in histogram.keys()], histogram.values(), 8)

plt.axis([-5, 105, 0, 5])

plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel(" # of Student")
plt.title("Distribution of Exam 1 Grades")
plt.show()


# # test 4

mentions = [500, 505]
years = [2013, 2014]

plt.bar([2012.6, 2013.6], mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of times I heard someone say 'data science' ")
plt.ticklabel_format(useOffset=False)
plt.axis([2012.5, 2014.5, 499, 506])
plt.title("Look at the 'Huge' Increase")
plt.show()

# test 5

plt.axis([2012.5, 2014.5, 5, 0, 550])
plt.title("Not So Huge Anymore")
plt.show()

xdata = [0, 1, 2, 4, 5, 8]
ydata = [0.1, 0.2, 0.4, 0.8, 0.6, 0.1]

plt.bar(xdata, ydata)
plt.show()
