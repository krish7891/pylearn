import numpy as np

a = np.arange(10)
print a

b = a[5]
print b

c = a[2:]
print c

d = a[2:5]
print d

k = np.array([[1,2,3], [3,4,5], [4,5,6]])
print k

print "Now we will slice the array from the index k[1:]"
print k[1:]

# this returns array of items in the second column
print 'The items in the second column are:'
print k[...,1]
print '\n'

# Now we will slice all items from the second row
print 'The items in the second row are:'
print k[1,...]
print '\n'

# Now we will slice all items from column 1 onwards
print 'The items column 1 onwards are:'
print k[...,1:]
