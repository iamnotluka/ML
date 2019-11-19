'''
Ordinary Least Squares Regression Algorithm

Linear regression also called OLS Regression is most
commonly used technique in Statistial Learning. It is
also the oldest.

'''

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import dataset
dataset = pd.read_csv('dataset.csv')
print('Ordinary Least Squares Regression Algorithm\n[+] Shape:', dataset.shape)
dataset.head()

# find relationship between the head size and brain weight

x = dataset['Head Size(cm^3)'].values
y = dataset['Brain Weight(grams)'].values

# calculate means of the data
x_mean = np.mean(x)
y_mean = np.mean(y)

# total number of values
n = len(x)

#use the formula to calculate b1 and b0 which are m and c in 'y = mx + c'
num = 0
den = 0

for i in range(n):
    num += (x[i] - x_mean) * (y[i] - y_mean)
    den += (x[i] - x_mean) ** 2

m = num/den
c = y_mean - (m * x_mean)

# displaying coeficients
print('\n[+] Coeficients\nm:', m,"\nc:", c)

# display relationship
print('\n\n[+] Brain Weights =', m, '* Head Size + ', c)

# plot the data
x_max = np.max(x) + 100
x_min = np.min(x) - 100

# calculate line values of x and y
X = np.linspace(x_min, x_max, 1000)
Y = m * X + c

# plotting line
plt.plot(X, Y, color = '#00ff00', label = 'Linear Regression')

# plot data points
plt.scatter(x, y, color='#ff0000', label = 'Data Points')

# labels
plt.xlabel('Head Size (cm^3)')
plt.ylabel('Brain Weight (grams)')

plt.legend()
plt.show()