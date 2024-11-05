class IceCream:
    def __init__(self, ingredient=None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def composition(self):
        if self.ingredient:
            print(f'Мороженое с {self.ingredient}')
        else:
            print('Обычное мороженое')


icecream = IceCream("шоколадом")
icecream.composition()
icecream = IceCream()
icecream.composition()
icecream = IceCream(5)
icecream.composition()