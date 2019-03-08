class Student:
    def __init__(self, x, y):
        self.name = x
        self.age= y



    def compare(self, a):
        if self.age == a.age:
            return True
        else:
            return False




c1=Student('sanjeev', 30)
c2=Student('om', 30)

if c1.compare(c2):
    print( 'same age')
else:
    print('different age')


