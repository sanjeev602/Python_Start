class student:
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3


    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        m3 = self.m3 + other.m3
        s3 = student(m1, m2, m3)
        return s3
    def __gt__(self, other):
        x = self.m1 + self.m2 + self.m3
        y = other.m1 + other.m2 + other.m3

        if x > y:
            return True
        else:
            return False
    def __str__(self):
        return '{} {} {}'.format (self.m1, self.m2, self.m3)

s1 = student(30,20,10)
s2 = student(50,10,30)

s3 = s1 + s2
print(s3.m1)

if s1.__gt__(s2):
    print('s1 is greater')
else:
    print(' s2 is greater')

print(s3)


