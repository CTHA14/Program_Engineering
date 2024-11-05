class Petr:
    __slots__ = ["name"]
    def __init__(self, name):
        if name == "Пётр":
            self.name = f"Да, я {name}"
        else:
            self.name = f"Нет, я не {name}, а Пётр"

person1 = Petr("Петров")
person2 = Petr("Пётр")
print(person1.name)
print(person2.name)