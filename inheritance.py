class A:
    def __init__(self):
        print('in A init')

    def feature1(self):
        print('in feature 1-A')

    def feature2(self):
        print('in feature 2')

class B:
    def __init__(self):
           print('in B init')

    def feature3(self):
        print('in feature 3')

    def feature4(self):
        print('in feature 4')

class C(A,B):
    def __init__(self):
        super().__init__()
        print('in c init')

c1 = C()
