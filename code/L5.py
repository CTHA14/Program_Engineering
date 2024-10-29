class Shape: #Основной класс
    def Area(self):
        pass

class Rectangle(Shape): #Класс-наследник
    def __init__ (self, w, h):
        self.w=w
        self.h=h
    
    def Area(self): #Унаследованый метод
        return self.w*self.h

class Circle(Shape): #Класс-наследник
    def __init__ (self, r):
        self.r=r
    
    def Area(self): #Унаследованый метод
        return 3.14*self.r*self.r