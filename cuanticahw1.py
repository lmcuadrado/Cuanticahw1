import numpy as np
import matplotlib.pyplot as plt

A=2
h=0.01
min_t = 0.0
max_t = 20.0

n= int((max_t - min_t)/h)

t = np.zeros(n)
x = np.zeros(n)
v = np.zeros(n)

#def oscilador(t,x):
#    return -A*x

t[0] = min_t
x[0] = 0.2
v[0] = 0.0

for i in range(0,n-1):
	t[i+1] = t[i] + h
	x[i+1] = x[i] + h * v[i]
	v[i+1] = v[i] - A*x[i]*h



plt.plot(t,x)
#plt.plot(t,v)
plt.show()

