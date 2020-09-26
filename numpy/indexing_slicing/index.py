import numpy as np 

x = np.array([[1, 2], [3, 4], [5, 6]]) 
print x
y = x[[0,1,2], [0,1,0]] 
print y


k = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 
   
print 'Our array is:' 
print k
print '\n' 

rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]]) 
z = k[rows,cols] 
   
print 'The corner elements of this array are:' 
print z
