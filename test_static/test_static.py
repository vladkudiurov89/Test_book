import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import cm

first_kind = [84.7, 105.0, 98.9, 97.9, 108.7, 81.3, 99.4, 89.4, 93.0, 119.3, 99.2, 99.4, 97.1, 112.4, 99.8, 94.7,
              114.0, 95.1,  115.5, 111.5]
second_kind = [57.2, 68.6, 104.4, 95.1, 89.9, 70.8, 83.5, 60.1, 75.7, 102.0, 69.0, 79.6, 68.9, 98.6, 76.0, 74.8,
               56.0, 55.6, 69.4, 59.5]
df = pd.DataFrame({'first_kind':first_kind, 'second_kind': second_kind})

print(f'1 median : {np.median(first_kind).round(3)}')
print(f'1 mean: {np.mean(first_kind)}')
print(f'1 variance: {np.var(first_kind).round(3)}')
print(f'1 std: {np.std(first_kind).round(3)}')

print(f'2 median: {np.median(second_kind)}')
print(f'2 mean: {np.mean(second_kind).round(3)}')
print(f'2 variance: {np.var(second_kind).round(3)}')
print(f'2 std: {np.std(second_kind).round(3)}')
print(stats.f_oneway(first_kind, second_kind))
print(stats.ttest_ind(first_kind, second_kind))

print(f'one anova: {stats.f_oneway(first_kind, second_kind)}')
print(f'T-student: {stats.ttest_ind(first_kind, second_kind)}')

sns.set()
sns.distplot(first_kind, kde=True)
plt.show()

sns.distplot(second_kind, kde=True)
plt.show()

sns.boxplot(data=df)
plt.show()

sns.boxplot(df["first_kind"])
print(f"1 describe:\n {df['first_kind'].describe()}")
plt.show()

sns.boxplot(df["second_kind"])
print(f"1 describe:\n {df['second_kind'].describe()}")
plt.show()


x, y = np.meshgrid(first_kind, second_kind)
r = np.sqrt(x ** 2 + y ** 2)
z = np.sin(r * 1.3)

ax = plt.figure(figsize=(8, 6))
ax = ax.add_subplot(1, 1, 1, projection='3d')
ax.plot_surface(x, y, z, cmap=cm.coolwarm, edgecolor='black', linewidth=0.23, antialiased=True)

plt.show()