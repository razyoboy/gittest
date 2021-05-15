import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as texas

x = np.array([2,3,4])
y = np.array([0.2239,-0.2601,-0.3971])
f = np.array([3.2])
m = np.array([])

n = len(x) - 1
j = 0
k = 0

for i in range(n):
    intm = (y[1+j]-y[0+j])/(x[1+j]-x[0+j])
    m = np.append(m, float(intm))
    j += 1
print(n)
print(m)


for f in f:
    inty = y[1+k] + (m[1+k]*(f-x[1]))

    print(inty)


g = texas.interp1d(x,y); print(g)