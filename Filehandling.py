f = open('data/mydata', 'a')
f.write('\n now we should have one more line')
f.close()

f=open('data/mydata')


print(f.read())