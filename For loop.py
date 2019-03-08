
for i in range(1,6):
    for j in range(1,i+1):
        print(' *', end='')
    for k in range(i+1, 11-i):
        print('  ',end='')
    for l in range(11-i, 11):
        print(' *', end='')


    print()

###################################

i = 0
while i <= 4:
    print('sanjeev', end='')
    j = 0
    while j <= 4:
        print(' alka', end='')
        j += 1

    print('')
    i += 1
