class Tomato:
    
    states = {'Отсутствует': 0, 'Цветение': 1, 'Зеленый': 2, 'Красный': 3}
    
    def __init__(self, index):
        self._index = index
        self._state = self.states['Отсутствует']
        
    def grow(self):
        if self._state < 3:
            self._state += 1
        
    def is_ripe(self):
        return True if self._state == 3 else False
 
class TomatoBush:
    
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(1, num+1)]
        
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()
            
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])
    
    def give_away_all(self):
        self.tomatoes = []
 
class Gardener:
    
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant
        
    def work(self):
        self._plant.grow_all()
        
    def harvest(self):
        if self._plant.all_are_ripe():
            print('Урожай собран!')
            self._plant.give_away_all()
        else:
            print('Томаты еще не дозрели')
            
    @staticmethod
    def knowledge_base():
        print('Справка по садоводству:')
        print('1. Не забывайте регулярно поливать и подкармливать растения')
        print('2. Определите правильное расстояние между растениями, чтобы они не мешали друг другу в росте')
        print('3. Удалите поврежденные листья и плоды, чтобы предотвратить распространение болезней')
 
Gardener.knowledge_base()