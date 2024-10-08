import matplotlib.pyplot as plt
import numpy as np

# Normal plot and scatter graphs
x_values = [1,2,3,4,5,6,7,8,9,10]
y_values = [1,4,6,8,10,12,14,16,18,20]

r'''
plt.plot(x_values,y_values, color='pink')
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Title")
plt.show()
'''

r'''
plt.scatter(x_values,y_values, color='pink')
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Title")
plt.show()
'''
# Bar chart
animal = ["cat", "dog", "horse", "mouse"]
animal_value = [10, 30, 100, 1]

r'''
plt.bar(animal, animal_value, color="black")
plt.xlabel("Animals")
plt.ylabel("Weight (kg)")
plt.title("Weight of species")
plt.show()
'''

# Histogram
X_normal = np.random.normal(0, 1, 100000)
plt.hist(X_normal, color="forestgreen")
plt.xlabel("X")
plt.ylabel("Frequency")
plt.title("Randomly Sampled Data")
plt.show()

from scipy.stats import norm
px_values = np.arange(-4, 4, 0.01)
py_values = norm.pdf(px_values)

counts, bins, ignored = plt.hist(X_normal, 30, density=True, color='red', label='Sampling Distribution')
plt.plot(px_values, py_values, color='yellow', linewidth=2.5, label='Population Distribution')
plt.title("Randomly generating 1000 obs from Normal Distribution mu = 0 sigma = 1")
plt.ylabel("Probability")
plt.legend()
plt.show()