'''
class Car:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f'{self.brand}: drive()')
'''

# another way to do it
def car_init(self, brand):
    self.brand = brand

def drive(self):
    print(f'{self.brand}: drive()')

Car = type('Car', (), {
    '__init__': car_init,
    'drive': drive
})

car = Car('Volvo')
car.drive()