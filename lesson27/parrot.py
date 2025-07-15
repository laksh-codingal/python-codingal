
class parrot:

    species = "bird"

    def __init__(self, name,  age):
        self.name = name
        self.age = age

parrot1 = parrot("laksh", 11)
parrot2 = parrot("vivaan", 9)

print("laksh is a", parrot1.species)
print("vivaan is a", parrot2.species)

print(parrot1.name, "is", parrot1.age, "years old")
print(f"{parrot2.name} is {parrot2.age} years old")
