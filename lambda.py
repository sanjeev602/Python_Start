from functools import reduce

lst = [1,3,6,3,4,8]

evens = list(filter(lambda n: n%2==0,lst))
print(evens)



sqr = list(map(lambda n: n*n, evens))
print(sqr)

result = reduce(lambda a,b: a+b, sqr)
print(result)






'''f1 = lambda a,b: a + b
f2 = lambda x, y: x*y

print(f1(3,4))
print(f2(4,5))
'''