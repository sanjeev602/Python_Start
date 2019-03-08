for i in range(1,21):
    if (i % 5 == 0) or (i % 3 == 0) :
        continue
    else:
        print (i)

    print(i, 'passed')