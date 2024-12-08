# Superclass: Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic animal sound."


# Derived class 1: Mammal
class Mammal(Animal):
    def __init__(self, name, has_fur=True):
        super().__init__(name)
        self.has_fur = has_fur

    def speak(self):
        return "I am a mammal sound."


# Derived class 2: Bird
class Bird(Animal):
    def __init__(self, name, can_fly=True):
        super().__init__(name)
        self.can_fly = can_fly

    def speak(self):
        return "I am a bird sound."


# Derived class using hybrid inheritance: Bat
class Bat(Mammal, Bird):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "I am a bat sound that combines mammal and bird-like traits."


# Testing the hybrid inheritance
bat_instance = Bat("Nocturno")
print(f"Name: {bat_instance.name}")
print(f"Type: Mammal & Bird")
print(bat_instance.speak())
