import pandas

# Creating a dictionary of lists
dfValues_1 = {'KEY': ['A_0', "A_1", "A_2", "A_3", "A_4", "A_5", "A_6"],
              "NAMES": ['ABI', "KAN", "ANN", "LIS", "BOB", "JAY", "ZED"],
              "AGE": [25, 37, 41, 18, 29, 31, 33]}

# Creating dataFrame_1 by calling DataFrame constructor with list as argument
dataFrame_1 = pandas.DataFrame(dfValues_1)

dfValues_2 = {'KEY': ['A_0', "A_1", "A_2", "A_3", "A_4", "A_5", "A_6"],
              'CITIES': ['MOSCOW', 'PARIS', 'RIM', 'MILAN', 'DELHI', 'NEW-YORK', 'CHICAGO']}

# Creating dataFrame_2 by calling DataFrame constructor with list as argument
dataFrame_2 = pandas.DataFrame(dfValues_2)

# Printing the dataframes
print('\nGiven dataFrame 1\n\n', dataFrame_1, '\nGiven dataFrame 2\n\n', dataFrame_2)

# Merging the dataframes using .merge() with UNIQUE KEY COMBINATION
new_DataFrame_1 = pandas.merge(dataFrame_1, dataFrame_2, on='KEY')

# Printing new dataframe_1
print('\nMerged dataFrame using one unique key\n\n', new_DataFrame_1)

# Creating a dictionary of lists
dfValues_1_1 = {'KEY': ['A_0', "A_1", "A_2", "A_3", "A_4", "A_5", "A_6"],
                'KEY_1': ['A_7', 'A_7', 'A_7', 'A_7', 'A_7', 'A_7', 'A_7'],
                "NAMES": ['ABI', "KAN", "ANN", "LIS", "BOB", "JAY", "ZED"],
                "AGE": [25, 37, 41, 18, 29, 31, 33]}

# Creating dataFrame_1_1 by calling DataFrame constructor with list as argument
dataFrame_1_1 = pandas.DataFrame(dfValues_1_1)

dfValues_2_2 = {'KEY': ['A_0', "A_1", "A_2", "A_3", "A_4", "A_5", "A_6"],
                'KEY_1': ['A_7', 'A_7', 'A_7', 'A_7', 'A_7', 'A_7', 'A_7'],
                'CITIES': ['MOSCOW', 'PARIS', 'RIM', 'MILAN', 'DELHI', 'NEW-YORK', 'CHICAGO']}

# Creating dataFrame_2_2 by calling DataFrame constructor with list as argument
dataFrame_2_2 = pandas.DataFrame(dfValues_2_2)

# Merging the dataframe by setting how argument to left (Keys from left frame)
new_DataFrame_2 = pandas.merge(dataFrame_1_1, dataFrame_2_2, on=['KEY', 'KEY_1'])

# Printing the new dataframe_2
print('\nMerged dataFrame using one unique key\n\n', new_DataFrame_2)

# Creating a dictionary of lists
dfValues_1_1_1 = {'KEY': ['A_0', "A_1", "A_2", "A_3", "A_4", "A_5", "A_6"],
                  'KEY_1': ['A_7', 'A_9', 'A_7', 'A_9', 'A_7', 'A_9', 'A_7'],
                  "NAMES": ['ABI', "KAN", "ANN", "LIS", "BOB", "JAY", "ZED"],
                  "AGE": [25, 37, 41, 18, 29, 31, 33]}

# Creating dataFrame_1_1_1 by calling DataFrame constructor with list as argument
dataFrame_1_1_1 = pandas.DataFrame(dfValues_1_1_1)


dfValues_2_2_2 = {'KEY': ['A_0', "A_1", "A_2", "A_3", "A_4", "A_5", "A_6"],
                  'KEY_1': ['A_7', 'A_9', 'A_7', 'A_9', 'A_7', 'A_9', 'A_7'],
                  'CITIES': ['MOSCOW', 'PARIS', 'RIM', 'MILAN', 'DELHI', 'NEW-YORK', 'CHICAGO']}

# Creating dataFrame_2_2_2 by calling DataFrame constructor with list as argument
dataFrame_2_2_2 = pandas.DataFrame(dfValues_2_2_2)

# Printing the dataframes
print('\nGiven dataFrame 1\n\n', dataFrame_1_1_1, '\nGiven dataFrame 2\n\n', dataFrame_2_2_2)

# Merging the dataframe by setting how argument to left (Keys from left frame)
leftMergeGF = pandas.merge(dataFrame_1_1_1, dataFrame_2_2_2, how='left', on=['KEY', "KEY_1"])

# Printing new the dataframe
print('\nLeft keys merged dataframe\n\n', leftMergeGF)

# Merging the dataframe by setting how argument to right (Keys from right frame)
rightMergeDF = pandas.merge(dataFrame_1_1_1, dataFrame_2_2_2, how='right', on=['KEY', "KEY_1"])

# Printing new the dataframe
print('\nRight keys merged dataframe\n\n', rightMergeDF)

# Merging the dataframe by setting how argument to outer (Union Of Keys)
outerMergeDF = pandas.merge(dataFrame_1_1_1, dataFrame_2_2_2, how='outer', on=['KEY', "KEY_1"])

# Printing new the dataframe
print('\nUnion keys merged dataframe\n\n', outerMergeDF)

# Merging the dataframe by setting how argument to inner (Intersection of Keys)
innerMergeDF = pandas.merge(dataFrame_1_1_1, dataFrame_2_2_2, how='inner', on=['KEY', "KEY_1"])

# Printing new the dataframe
print('\nIntersection of Keys  merged dataframe\n\n', innerMergeDF)