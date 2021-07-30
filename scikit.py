import numpy as np 
import matplotlib
import matplotlib.pyplot as plt

from sklearn import linear_model

# Random data
A = np.array([[2, 5, 7, 9, 13, 16, 18, 20, 24, 29, 34, 37, 39, 40]]).T
b = np.array([[2, 3, 6, 8, 10, 12, 19, 25, 23, 30, 32, 33, 44, 46]]).T

# Create model
lr = linear_model.LinearRegression()
# Fit (train the model)
lr.fit(A, b)

# y = ax + b, a: coefficent, b: intercept
print(lr.coef_)
print(lr.intercept_)

# Draw random data
plt.plot(A, b, 'ro')

x0 = np.array([[1,46]]).T
y0 = x0*lr.coef_ + lr.intercept_

# Draw line
plt.plot(x0, y0)

plt.show()