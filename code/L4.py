class car: #Создание класса
    def __init__(self, manufac, model): #Создание атрибутов класса
        self._manufac=manufac #protected атрибут
        self.__model=model #private атрибут

    def drive(self): #Создание метода класса
        print(f"Driving {self._manufac} {self.__model}")

my_car=car("Audi", "A6") #Создание экземпляра класса
print(my_car._manufac)
my_car.drive() #Вызов метода класса