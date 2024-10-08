import pandas as pd

data = pd.DataFrame({'A1': [1, 2, 3],
                     'A2': [4, 5, 6],
                     'A3': [7, 8, 9]},
                    index = ['X', 'Y', 'Z'])

print(data)

print(data.loc['Y'])

print(data.loc[:,'A2'])

print(data.loc['Z', 'A3'])