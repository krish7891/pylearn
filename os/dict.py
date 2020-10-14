#!/usr/bin/python

seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq)
print "New Dictionary : %s" %  str(dict)

dict = dict.fromkeys(seq, ['Kishan', 30, 'Male'])
print "New Dictionary : %s" %  str(dict)
