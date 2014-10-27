class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print('Hello. My name', self.name)

p = Person('Dred')
p.sayHi()