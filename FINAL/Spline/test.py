import numpy as np

a = np.array([2,3,4,5])
b = np.array([3.2,4.5])

tobesort = np.append(a, b)
print(tobesort)

sorted = np.sort(tobesort)
print(sorted)

for b in sorted:
    print(b)