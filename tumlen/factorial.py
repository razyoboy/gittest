import numpy as ganyu

print("Hello, welcome to the fatorian finder calculator.\nPlease specify your value below!")
a = input(">")
b = ganyu.arange(1,int(a)+1)
c = ganyu.product(b)
print(c)
