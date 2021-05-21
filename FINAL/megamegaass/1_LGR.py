import numpy as np
import matplotlib.pyplot as plt

x = np.array([5,8,10,12,14,16,18,13.75])
y = np.array([10989,18959,47019,98519,183875,315423,507419])

def LGR(x,y):
    l0 = ((x[-1]-x[1])/(x[0]-x[1]))*((x[-1]-x[2])/(x[0]-x[2]))*((x[-1]-x[3])/(x[0]-x[3]))*((x[-1]-x[4])/(x[0]-x[4]))*((x[-1]-x[5])/(x[0]-x[5]))*((x[-1]-x[6])/(x[0]-x[6]))
    l1 = ((x[-1]-x[0])/(x[1]-x[0]))*((x[-1]-x[2])/(x[1]-x[2]))*((x[-1]-x[3])/(x[1]-x[3]))*((x[-1]-x[4])/(x[1]-x[4]))*((x[-1]-x[5])/(x[1]-x[5]))*((x[-1]-x[6])/(x[1]-x[6]))
    l2 = ((x[-1]-x[0])/(x[2]-x[0]))*((x[-1]-x[1])/(x[2]-x[1]))*((x[-1]-x[3])/(x[2]-x[3]))*((x[-1]-x[4])/(x[2]-x[4]))*((x[-1]-x[5])/(x[2]-x[5]))*((x[-1]-x[6])/(x[2]-x[6]))
    l3 = ((x[-1]-x[0])/(x[3]-x[0]))*((x[-1]-x[1])/(x[3]-x[1]))*((x[-1]-x[2])/(x[3]-x[2]))*((x[-1]-x[4])/(x[3]-x[4]))*((x[-1]-x[5])/(x[3]-x[5]))*((x[-1]-x[6])/(x[3]-x[6]))
    l4 = ((x[-1]-x[0])/(x[4]-x[0]))*((x[-1]-x[1])/(x[4]-x[1]))*((x[-1]-x[2])/(x[4]-x[2]))*((x[-1]-x[3])/(x[4]-x[3]))*((x[-1]-x[5])/(x[4]-x[5]))*((x[-1]-x[6])/(x[4]-x[6]))
    l5 = ((x[-1]-x[0])/(x[5]-x[0]))*((x[-1]-x[1])/(x[5]-x[1]))*((x[-1]-x[2])/(x[5]-x[2]))*((x[-1]-x[3])/(x[5]-x[3]))*((x[-1]-x[4])/(x[5]-x[4]))*((x[-1]-x[6])/(x[5]-x[6]))
    l6 = ((x[-1]-x[0])/(x[6]-x[0]))*((x[-1]-x[1])/(x[6]-x[1]))*((x[-1]-x[2])/(x[6]-x[2]))*((x[-1]-x[3])/(x[6]-x[3]))*((x[-1]-x[4])/(x[6]-x[4]))*((x[-1]-x[5])/(x[6]-x[5]))

    f0 = y[0]; f1=y[1];f2=y[2];f3=y[3];f4=y[4];f5=y[5];f6=y[6]
    inty = (l0*f0)+(l1*f1)+(l2*f2)+(l3*f3)+(l4*f4)+(l5*f5)+(l6*f6)
    y = np.append(y, float(inty))
    return y

ymod = LGR(x,y)
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

plt.title('Polynomial (Higher Order) LGR Interpolation Results')
plt.show()

#github.com/razyoboy/unishared