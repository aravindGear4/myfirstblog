class fruit:
    print('this is weird python')
    def __init__(self, clr):
        self.color=clr
    def printColor(self):
        print(self.color)
ob1=fruit("red")
ob1.hasSeed=False
print(ob1.color)
print(type(ob1.printColor))
for line in open('admin.py'):
    print(line)