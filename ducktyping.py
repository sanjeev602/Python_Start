class pycharm:
    def execute(self):
        print('typing')
        print('compling')
class youreditor:
    def execute(self):
        print('nothing')
        print('compling')
class myeditor:
    def execute(self):
        print('editing')
        print('xpediting')
        print('running')
        print('typing')
        print('compling')

class comp:
    def code(self,ide):
        ide.execute()

ide=youreditor()

c1 = comp()
c1.code(ide)

