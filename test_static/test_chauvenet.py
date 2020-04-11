import numpy as np
from scipy import special
# Chauvenet


def get_chauvenet(date, value):
    mean_date = np.mean(date)
    std_date = np.std(date)
    compare = 1 / (2 * len(date))
    if value not in date:
        print('ERROR')

    result = special.erfc(np.abs(value - mean_date) / std_date)

    if result < compare:
        print("This is ejection")
    else:
        print("This is not ejection")

    # print(compare)
    # print(result)
    return date.remove(value)


# sample
date_test = [8.02, 8.16, 3.97, 8.64, 0.84, 4.46, 0.81, 7.74, 8.78, 9.26, 20.46, 29.87, 10.38, 25.71]
get_chauvenet(date_test, 25.71)
get_chauvenet(date_test, 29.87)
get_chauvenet(date_test, 20.46)
get_chauvenet(date_test, 10.38)
