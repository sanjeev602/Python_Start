def count(lst):
    even =0
    odd=0
    for i in lst:
        if i%2 ==0:
            even += 1
        else:
            odd += 1
    return(even, odd)

lst= [12,20,30,14,43,37,75]
even, odd = count(lst)

print('even : {}, odd: {}'.format(even, odd))
