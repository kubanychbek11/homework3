class First:
    def __init__(self,name):
        self.name = name
class Second:
    def __init__(self,age):
        self.age = age
class Third:
    def metod1(self):
        print('world')
class Fourth:
    def metod2(self):
        print('hello')
class Fifth(First, Second,Third, Fourth):
    def __init__(self,name,age):
        Second.__init__(self,age)
        First.__init__(self,name)

stay= Fifth('qwer',12 )
stay.metod1()
stay.metod2()

