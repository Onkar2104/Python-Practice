from array import *
vals = array('i',[2,3,4,5])
newarr=array(vals.typecode,(x*x for x in vals))
print(newarr)
i=0
while i<len(newarr):
     print(newarr[i])
     i+=1