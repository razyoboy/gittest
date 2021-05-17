import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,12,13,18,21,24,13.75])
y = np.array([-1,98519,136239,507419,944663,1617455])

def three(x,y):
    n = len(x)-7
    
    c0 = y[0]; print(c0)
    c1 = (y[1] - y[0])/(x[1]-x[0]); print(c1)
    c2 = ((((y[2] - y[1])/(x[2] - x[1])) - ((y[1] - y[0]) / (x[1]-x[0])))) / (x[2] - x[0])
    c3 = (((y[3] - y[2] - y[1])/(x[3]-x[2]-x[1])) - (y[2]-y[1]-y[0])/(x[2]-x[1]-x[0])) / (x[3]-x[0])
    c4 = (((y[4]-y[3]-y[2]-y[1])/(x[4]-x[3]-x[2]-x[1])) - ((y[3]-y[2]-y[1]-y[0])/(x[3]-x[2]-x[1]-x[0])))/(x[4]-x[0])
    c5 = (((y[5]-y[4]-y[3]-y[2]-y[1])/(x[5]-x[4]-x[3]-x[2]-x[1])) - ((y[4]-y[3]-y[2]-y[1]-y[0])/(x[4]-x[3]-x[2]-x[1]-x[0])))/(x[5]-x[0])
    #c6 = (((y[6]-y[5]-[4]-y[3]-y[2]-y[1])/(x[6]-x[5]-x[4]-x[3]-x[2]-x[1])) - ((y[5]-y[4]-y[3]-y[2]-y[1]-y[0])/(x[5]-x[4]-x[3]-x[2]-x[1]-x[0])))/(x[6]-x[0])
    diffc1 = (x[-1]-x[0])
    diffc2 = (x[-1]-x[0])*(x[-1]-x[1])
    diffc3 = (x[-1]-x[0])*(x[-1]-x[1])*(x[-1]-x[2])
    diffc4 = (x[-1]-x[0])*(x[-1]-x[1])*(x[-1]-x[2])*(x[-1]-x[3])
    diffc5 = (x[-1]-x[0])*(x[-1]-x[1])*(x[-1]-x[2])*(x[-1]-x[3])*(x[-1]-x[4])
    #diffc6 = (x[-1]-x[0])*(x[-1]-x[1])*(x[-1]-x[2])*(x[-1]-x[3])*(x[-1]-x[4])*(x[-1]-x[5])
    inty = c0 + (c1*diffc1) + (c2*diffc2) + (c3*diffc3) + (c4*diffc4) + (c5*diffc5)
    print(inty)
    y = np.append(y, float(inty))
    return y

ymod = three(x,y)
print(f"Interpolated values are (x,y);")
w = len(ymod)
p = 0
for k in range (w-1):
    print(f"(X{p},Y{p}) -> ({x[0+p]}, {ymod[0+p]})")
    p += 1

ans = ymod[-1]
exact = 170950.8
err = abs(((exact - ans)/exact) * 100)
print(f"Error percentage is {err}%")

print(f"(Xint,Yint) -> ({x[-1]}, {ymod[-1]})")
plt.scatter(x,ymod)
plt.xlabel('x')
plt.ylabel('f(x)')

for xs,ys in zip(x,ymod):
    xout = "{:.2f}".format(xs)
    yout = "{:.2f}".format(ys)
    label = f"({xout},{yout})"
    plt.annotate(label, (xs,ys))

plt.title('Polynomial (Higher Order) NDD Interpolation Results')
plt.show()

