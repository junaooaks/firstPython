class Car:

    def __init__(self):
        self.color = 'red'
        self.year = 2020
        self.make = 'volks'
        self.name = 'passat'

    def drive(self):
        print(self.name + ': started')

    @staticmethod
    def hello(x):
        print(x + ' : cool staticmenthod')

    @classmethod
    def show(cls):
        print(cls.x)
