lst = [3,1,4,9,4,1,5, 0, 2 , 33, 1]
x= 1
while x <= len(lst) - 1:
    y = 0
    while y <= len(lst) -1 - x:




        if lst[y] > lst[y+1]:
            t = lst[y]
            lst[y] = lst[y+1]
            lst[y+1] =t
        y += 1
    x += 1

print(lst)
