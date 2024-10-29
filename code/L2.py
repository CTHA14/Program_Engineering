class car: #Создание класса
    def __init__(self, manufac, model): #Создание атрибутов класса
        self.manufac=manufac 
        self.model=model 

    def drive(self): #Создание метода класса
        print(f"Driving {self.manufac} {self.model}")

my_car=car("Audi", "A6") #Создание экземпляра класса
my_car.drive() #Вызов метода класса