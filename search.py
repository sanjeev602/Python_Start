pos = -1
def search(list, x):

    for i in list:
        globals()['pos'] += 1
        if i == x:
            return True
    return False


list= [10,20,30,5,30, 400, 1]
n = 400

if search(list,n):
    print('the elements has been found at position:', pos)
else:
    print('the elements is mising')