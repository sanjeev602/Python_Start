class A:
    def show(self):
        print('in Show-A')

class B(A):
    def show(self):
        print('in show B')

b1 = B()
b1.show()