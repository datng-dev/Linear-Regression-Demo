import numpy as np 
import matplotlib
import matplotlib.pyplot as plt

#random data
A = [2, 5, 7, 9, 13, 16, 18, 20, 24, 29, 34, 37, 39, 40]
b = [2, 3, 6, 15, 22, 28, 34, 36, 40, 37, 35, 31, 28, 25]

# Visualize data
plt.plot(A, b, 'ro') # Ve ra cac diem voi toa do la (x, y)

# Change row vector to colum vector
A = np.array([A]).T
b = np.array([b]).T

# Create A square
# print(A[:, 0]) # In tat ca cac so ở cột 0 trong ma tran A theo hang ngang
x_square = np.array([A[:, 0]**2]).T

# Combine x_square and A
A = np.concatenate((x_square, A), axis=1)

# Create vector 1
ones = np.ones((A.shape[0], 1), dtype=np.int8) # np.ones() la ham dac biet tao toan vecto 1

# Combine 1 and A
A = np.concatenate((A, ones), axis=1) 
print(A)

# Use fomular
x = np.linalg.inv(A.transpose().dot(A)).dot(A.transpose()).dot(b) # (A.T*A)^-1*A.T* => tim dc x la gia tri a,b,c trong y = ax^2 + bx +c

#Ve parabole y = ax^2 + bx +c, test data to draw
x0 = np.linspace(1, 45, 10000) # x0 chua 10000 diem tu 1 den 45, x0.shape = (10000,)
y0 = x[0][0]*x0*x0 + x[1][0]*x0 + x[2][0]
print(y0)

plt.plot(x0, y0)


plt.show()