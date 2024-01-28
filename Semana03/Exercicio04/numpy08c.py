import numpy as np

a = np.array([[1,2],[3,4],[5,6]])
print(a)

print(a[a>2])

b = np.where(a>2, a, -1)
print(b)