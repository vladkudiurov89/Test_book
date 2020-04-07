import pandas as pd
from sklearn.metrics import mean_absolute_error
import numpy as np

test_name = pd.Series(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
Y = pd.Series([1, 2, 3, 4, 5, -1, -2, -3, -4, -5])
Y_pred = pd.Series([0, 2, 2, 5, 3, -1, -1, -4, -6, -5])

table = pd.DataFrame({'Name': test_name, "Y": Y, 'Y_pred': Y_pred})
print(table)

mae_value = mean_absolute_error(table['Y'], table['Y_pred'])
print(mae_value)


def get_MAPE(y_true, y_pred):
    return (np.mean(np.abs((y_true - y_pred) / y_true))) * 100


print(get_MAPE(table['Y'], table['Y_pred']).round(0))

