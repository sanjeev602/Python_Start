fname='Sanjeev'
mname='kumar'
lname='Pathak'

sname= ' '
name= fname + sname+ mname + sname+ lname

print(name)

x= len(name)

print('length of the name is ', x)
print('lets print the name in reverse order')

count = x - 1
while count >= 0:
    print(name[count],end='')
    count -= 1
print("")
print('bye...')

