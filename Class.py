class Student:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        self.lap=self.Laptop()


    def show(self):
        print(self.name, self.age)
        self.lap.show_laptop()


    class Laptop:
        def __init__(self):
            self.brnd ='hp'
            self.cpu = 'I5'
        def show_laptop(self):
            print(self.brnd, self.cpu)


s1=Student('sanjeev',32)
s2=Student('alka', 30)

s1.show()
print(s1.lap.brnd)


















'''class Student:

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3


    def average(self):
        return((self.m1+self.m2+self.m3)/3)

    def get_m1(self):
        return self.m1
    
    def set_m1(self):
        self.m1 = 0


s1=Student(20,30,40)
s2=Student(80,90,75)

print(s1.average())
print(s2.average())
print(s1.get_m1())
s1.set_m1()
print(s1.get_m1())

'''
