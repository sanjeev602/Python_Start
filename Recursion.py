def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

print(fact(5))




'''result = 1

def fact(x):
  global result
  result = result * x
  x = x -1
  if x > 0:
      fact(x)

y = int(input('please enter the number:'))
fact(y)
print('factorial value of', y, 'is:', result)
'''


'''import sys

print (sys.getrecursionlimit())
sys.setrecursionlimit(200)
i =0
def initial():
    global i
    i  +=1
    print('hello', i)
    initial()

initial()
'''
