import numpy as np

x = np.array([[0 ,1, 2], [3, 4, 5], [6, 7,8], [9, 10, 11], [12, 13, 14], [15, 16, 17]])

print x

#slicing
#Tec : Niche lakhela no matlab?
# 2nd row jya row starts from 0
# 1st col where col starts from 0
# show data till 4 row and 3 col
z = x[2:4, 1:3]

print "After slicing out arr becomes\n"

print z

print "Now we will try boolean indexing"

print x[x>4]

print "NaN (Not a Number) elements are omitted by using ~ (complement operator)."

a = np.array([np.nan, 1,2,np.nan,3,4,5])
print a[~np.isnan(a)]

print "Now filter complex number"
a = np.array([1, 2+6j, 5, 3.5+5j])
print a[np.iscomplex(a)]
