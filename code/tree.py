import abc
import random
from fruit import *
class Tree(metaclass=abc.ABCMeta):
    def __init__(self, sort, max_fruits, speed):
        self._fruits = []
        self._sort = sort
        self._max_fruits = max_fruits
        self._speed = speed

    def make_fruits(self):
        pass
        
    def notify(self, event):
        [fruit.state.update(event) for fruit in self._fruits]

    def drop_fruits(self):
        self._fruits = [x for x in self._fruits if not isinstance(x.state, Overgrowth_State)]
    
    def harvested(self):
        for fruit in self._fruits:
                if fruit.readiness > 80:
                    self._fruits.remove(fruit)
    
class Apple_Tree(Tree):
    def __init__(self, sort, max_fruits, speed):
        super().__init__(sort, max_fruits, speed)

    def make_fruits(self):
        if(self._max_fruits > len(self._fruits) + self._speed):
            self._fruits.extend([Apple(self._sort) for _ in range(self._speed)])
        else:
            self._fruits.extend([Apple(self._sort) for _ in range(self._max_fruits - len(self._fruits))])

class Cherry_Tree(Tree):
    def __init__(self, sort, max_fruits, speed):
        super().__init__(sort, max_fruits, speed)

    def make_fruits(self):
        if(self._max_fruits > len(self._fruits) + self._speed):
            self._fruits.extend([Cherry(self._sort) for _ in range(self._speed)])
        else:
            self._fruits.extend([Cherry(self._sort) for _ in range(self._max_fruits - len(self._fruits))])

class Tree_Creator(metaclass = abc.ABCMeta):
    def get_tree(self, sort):
        tree = self.create_tree(sort)
        return tree

    def set_speed(self, sort):
        self.speed_to_set = random.randint(5, 10) + sort * 5
    
    def set_max_fruit(self, sort):
        self.max_fruit_to_set = random.randint(30, 40) + sort * 5

    def create_tree(self, sort):
        self.set_max_fruit(sort)
        self.set_speed(sort)

class Apple_Tree_Creator(Tree_Creator):
    def create_tree(self, sort):
        super().create_tree(sort)
        return Apple_Tree(sort, self.max_fruit_to_set, self.speed_to_set)

class Cherry_Tree_Creator(Tree_Creator):
    def set_speed(self, sort):
        super().set_speed(sort * 2)
        self.speed_to_set *= 3
    
    def set_max_fruit(self, sort):
        super().set_max_fruit(sort * 2)
        self.max_fruit_to_set *= 3
    
    def create_tree(self, sort):
        super().create_tree(sort)
        return Cherry_Tree(sort, self.max_fruit_to_set, self.speed_to_set)
