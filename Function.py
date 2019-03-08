def person(name, **data):
    print(name)
    for i, j in data.items():
        print(i,j)





person('sanjeev', age=28, city='mumbai', mobile=9910319388)









'''def addition(*b):
    result = 0
    for x in b:
        result = result + x
    print(result)

addition(2, 5, 3, 34, 30, 45)
'''

'''def named(name,age=20):
    print(name)
    print(age - 10)

named( name='Sanjeev')
'''


'''def add(a, b):
    c = a + b
    return c

result = add(10, 20)
print('addition of numbers =', result )
'''


'''def count(list1):
    even = []
    odd = []

    for i in list1:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return(even, odd)

list1= [10,12,34,20,5,3,9,5]

x, y = count(list1)
print ('even:', x)
print('odd:', y)
'''



'''def personal(name, **data):
    print(name)
    for i, j in data.items():
        print(i,  j)

personal('sanjeev', age=28, hometown='azam', live='mumbai')
'''


'''def sum(a, *b):
    print(a)
    print(b)
    for i in b:
        a = a + i
    print('sum:', a)

sum(1, 2 , 3, 4)'''

'''def simple():
    print('this is a simple function program to get addition value')

def add(*b):
    a = 0
    for i in b:
        a = a + i
    return(a)


simple()
result= add( 1, 2, 4, 5,7)
print(result)'''












