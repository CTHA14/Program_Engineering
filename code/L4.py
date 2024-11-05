class Mammal:
    className = "Mammal"

class Dog(Mammal):
    species = "canine"
    sounds = "wow"
    LovedToy = "stick"

class Cat(Mammal):
    species = "feline"
    sounds = "meow"
    LovedToy = "rope"

dog = Dog()
print(f"Dog is {dog.className}, but it says {dog.sounds}. Dogs like to play with {dog.LovedToy}.")
cat = Cat()
print(f"Cat is {cat.className}, but it says {cat.sounds}. Cats like to play with {cat.LovedToy}.")