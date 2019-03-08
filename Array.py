from array import *

val = array('i',[10,20,30,40])

newval = array(val.typecode,(a*a for a in val))

for k in newval:
    print(k)

