class Doggo:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
miles = Doggo("Miles", 4)
buddy = Doggo("Buddy", 9)
jack = Doggo("Jack", 3)
jim = Doggo("Jim", 5)

# create inherited class  and its instance 

class Labrador(Doggo):
    pass

gandhi = Labrador("Gandhi", 13)

print(gandhi.name, gandhi.age)
print(gandhi.species)
print(gandhi)
gandhi.speak("buf")
print(isinstance(gandhi, Labrador))

print(isinstance(gandhi, Doggo))

# Extending a Parent CLass
class JackRusselTerrier(Doggo):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"
    
miles = JackRusselTerrier("Miles", 4)
miles.speak()
miles.speak("Grr")
