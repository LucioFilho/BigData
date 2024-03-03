#inheritance
class Pet:
    def __init__(self, animal, specie, name, age, sound, owner):
        self.animal = animal
        self.specie = specie
        self.name = name
        self.age = age
        self.sound = sound
        self.the_owner = owner

# creating a dog blueprint 
class Dog(Pet):
    def barking(self):
        return f"{self.name} is {self.age} years old and he says {self.sound} when he sees his owner {self.the_owner}"

# Creating an object of the Dog class
john_dog = Dog(animal = 'Mammal', specie = 'Dog', name = 'Buddy', age = 4, sound = 'ouou', owner = 'John')
print(john_dog.barking())  # Buddy says ouou!

bob_dog = Dog(animal = 'Mammal', specie = 'Dog', name = 'Ted', age=3, sound = 'woof', owner = 'Bob')
print(bob_dog.barking())  # Ted says woof!

lisa_dog = Dog(animal = 'Mammal', specie = 'Dog', name = 'Zeus', age=7, sound = 'wow', owner = 'Lisa')
print(lisa_dog.barking())  # Zeus says wow!

