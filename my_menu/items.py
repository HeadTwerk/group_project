# general Item class for every food item
class Item:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

# different types of food item

class Drink(Item):
    def __init__(self, name, cost, taste):
        super().__init__(name, cost)
        self.taste = taste

class Rice(Item):
    def __init__(self, name, cost, length):
        super().__init__(name, cost)
        self.length = length

class Chappati(Item):
    def __init__(self, name, cost, type):
        super().__init__(name, cost)
        self.type = type

class Paneer(Item):
    def __init__(self, name, cost, taste):
        super().__init__(name, cost)
        self.taste = taste

class Chicken(Item):
    def __init__(self, name, cost, taste):
        super().__init__(name, cost)
        self.taste = taste







