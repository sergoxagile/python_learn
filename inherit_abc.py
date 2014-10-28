from abc import *
class SchoolMember(metaclass=ABCMeta):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('School member created: {}'.format(self.name))
    def tell(self):
        print('Name:"{}", Age:"{}"'.format(self.name, self.age))

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Create Teacher: {}'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Salary: {:d}'.format(self.salary))

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('Created Student: {}'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Marks: {:d}'.format(self.marks))

t = Teacher('Vasiliev', 40, 30000)
s = Student('Dred', 27, 100)

members = [t, s]

for member in members:
    member.tell()