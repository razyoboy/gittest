import numpy as np
import matplotlib.pyplot as plt

x = np.array([2,4,3.2])
y = np.array([0.2239,-0.3971])
'''
print("Please input your x-values (x-axis) [Minimum of Two] \n When done please type 'a'")

while True:
    xint = input('> ')
    if xint.isnumeric() == True:
        x = np.append(x, float(xint))
    elif xint.lower() == 'a':
        break

print("Please inout your f(x)-values (y-axis) [NO MORE than Two]\n When done please type 'a'")

while True:
    yint = input('> ')
    if yint.isnumeric() == True:
        y = np.append(y, float(yint))
    elif yint.lower() == 'a':
        break
'''
def NDD(x,y):
    n = len(x) - 2
    j = 0
    for i in range (n):
        c0 = y[0+j]
        c1 = (y[1+j] - y[0+j]) / (x[1+j] - x[0+j])
        diff = x[2+j] - x[0+j]
        inty = c0 + (c1*diff)
        j += 1
        y = np.append(y, float(inty))
    return y

ymod = NDD(x,y)

print(f"Interpolated values are (x,y);")
w = len(y)
p = 0
for k in range (w):
    print(f"(X{p},Y{p}) -> ({x[0+p]}, {y[0+p]})")
    p += 1

plt.scatter(x,ymod)
plt.plot(x,ymod)
plt.xlabel('x')
plt.ylabel('f(x)')
for x,y in zip(x,ymod):
    label = "{:.2f}".format(y)
    plt.annotate(label, (x,y))
plt.title('Linear NDD Interpolation Results')
plt.show()