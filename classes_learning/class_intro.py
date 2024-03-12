class Creature:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
    
    def attack(self, amount):
        self.energy -= 20
    
    def move(self, speed):
        pass

creature1 = Creature(10, 20)
