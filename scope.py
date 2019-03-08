a = 20

def afx():
    a = 23
    print (a)
    globals()['a'] = 50


afx()
print(a)