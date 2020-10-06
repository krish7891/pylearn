import numpy as np

a = np.arange(0, 60, 5)
a = a.reshape(3,4)

print 'Original Array is :'
print a

print 'Transpose of original array is'
b = a.T
print b

print 'Modified array is :'
for x in np.nditer(b):
    print x,
