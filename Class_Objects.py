class student:
    def __init__(self, name, age, subject):
        self.name=name
        self.age=age
        self.subject = subject



    def study(self):
        print(self.name, self.age,self.subject)

stu1 = student('sanjeev', 38, 'math')
stu2 = student('alka', 22, 'english')

stu1.study()
stu2.study()
