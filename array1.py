from array import *

val = array('i',[])

while True:
    res = int(input('enter the numbers to store 1st:'))

    if (res % 7 == 0):
        break
    else:
        val.append(res)

print(val)

tosearch = int(input('please enter the value u want to search:'))

k = 0
while k < len(val):
    if tosearch == val[k]:
        print('number found at index:', k)
    k += 1

print(val.index(tosearch))

print('bood bye...')