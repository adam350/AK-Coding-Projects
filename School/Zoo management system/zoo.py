class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Mammal(Animal):
    def make_sound(self):
        return "Roar!"

class Bird(Animal):
    def make_sound(self):
        return "Chirp!"

lion = Mammal("Scar", 7)
parrot = Bird("Rio", 4)

print(f"{lion.name} the Mammal makes a sound: {lion.make_sound()}")
print(f"{parrot.name} the Bird makes a sound: {parrot.make_sound()}")