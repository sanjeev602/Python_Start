lst = [3,5,9,1,3,6]
for i in range(0,len(lst)-1, 1):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            tem= lst[i]
            lst[i] = lst[j]
            lst[j] =tem

print (lst)