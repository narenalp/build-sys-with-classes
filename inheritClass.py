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