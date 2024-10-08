import numpy as np
import pandas as pd
from scipy import stats

data = [100, 20, 5, 20, 45, -100, 46]

print(np.median(data))
print(np.mean(data))

print(stats.mode(data))

print(np.var(data))
print(np.std(data))

data_csv = pd.read_csv("percent-bachelors-degrees-women-usa.csv")
print(data_csv.describe())