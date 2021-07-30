import numpy as np 
import matplotlib
import matplotlib.pyplot as plt

#random data
A = [2, 5, 7, 9, 13, 16, 18, 20, 24, 29, 34, 37, 39, 40]
b = [2, 3, 6, 8, 10, 12, 19, 25, 23, 30, 32, 33, 44, 46]

# Visualize data
plt.plot(A, b, 'ro') # Ve ra cac diem voi toa do la (x, y)

# Change row vector to colum vector
A = np.array([A]).T
b = np.array([b]).T

# Create vector 1
ones = np.ones((A.shape[0], 1), dtype=np.int8) # np.ones() la ham dac biet tao toan vecto 1

# Combine 1 and A
A = np.concatenate((A, ones), axis=1) 
print(A)

# Use fomular
x = np.linalg.inv(A.transpose().dot(A)).dot(A.transpose()).dot(b) # (A.T*A)^-1*A.T* => tim dc x la gia tri a,b trong y = ax + b

#Ve duong thang y = ax + b, test data to draw
x0 = np.array([[1,46]]).T
y0 = x0*x[0][0] + x[1][0]
print(y0)

plt.plot(x0, y0)

# Test predicting data
x_test = 12
y_test = x_test*x[0][0] + x[1][0]

plt.show()