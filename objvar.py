class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print('Init {}'.format(self.name))
        Robot.population += 1

    def __del__(self):
        print('{} delited'.format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print('{} was last'.format(self.name))
        else:
            print('{} robots more'.format(Robot.population))

    def sayHi(self):
        print('Hello my loard. My name is {}'.format(self.name))

    @staticmethod
    def howMany():
        print('You have {} robots'.format(Robot.population))


droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()
droid2 = Robot('C-3PO')
droid2.sayHi()
Robot.howMany()

del droid1
del droid2