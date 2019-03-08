class Cal:
    s = 0
    def add(self, x=None, y=None, z=None):
        if x != None and y != None and z!= None:
            s = x+y+z



        elif x != None and y != None:
            s = x + y
        else:
            s = x
        return s

c1 = Cal()
print(c1.add(2))


