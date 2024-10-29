class car: #Создание класса
    def __init__(self, manufac, model): #Создание атрибутов класса
        self.manufac=manufac 
        self.model=model 

    def drive(self): #Создание метода класса
        print(f"Driving {self.manufac} {self.model}")

my_car=car("Audi", "A6") #Создание экземпляра класса
my_car.drive() #Вызов метода класса

class electricCar(car): #Создание класса-наследника
    def __init__(self, manufac, model, capacity):
        super().__init__(manufac, model)
        self.capacity=capacity
    
    def charge(self):
        print(f"Charging {self.manufac} {self.model} with {self.capacity} kWh charger")

my_el_car=electricCar('Tesla', 'Model X', 100)
my_el_car.drive()
my_el_car.charge()