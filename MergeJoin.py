import pandas as pd

# Creating 2 dataframes

data1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
                      'VALUE1': [1, 2, 3, 4, 5, 6, 7]})

data2 = pd.DataFrame({'key': ['C', 'D', 'E', 'F', 'G', 'H'],
                      'VALUE2': [8, 9, 10, 11, 12, 13]})

print(data1)
print(data2)

# Inner Merge Join
print(pd.merge(data1, data2, on='key', how='inner'))

# Left join
print(pd.merge(data1, data2, on='key', how='left'))

# Right join
print(pd.merge(data1, data2, on='key', how='right'))

# Left anti-join
merged_left = pd.merge(data1, data2, on='key', how='left', indicator=True)
print(merged_left[merged_left["_merge"] == "left_only"])

# Right anti-join (with tables dropped)
merged_right = pd.merge(data1, data2, on='key', how='right', indicator=True)
anti_join_right = merged_right[merged_right["_merge"] == "right_only"]
anti_join_right = anti_join_right.drop("_merge", axis=1)
print(anti_join_right)