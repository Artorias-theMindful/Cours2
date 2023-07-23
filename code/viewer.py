import abc
from fruit import *
class Info(metaclass=abc.ABCMeta):
    def __init__(self):
        self.fruits = []
    
    def update(self, garden):
        pass

    def show_info(self, garden):
        pass

class Harvested_Info(Info):
    def __init__(self):
        super().__init__()
    
    def update(self, garden):
        self.fruits.extend([fruit for tree in garden.trees for fruit in tree._fruits if isinstance(fruit.state, Ready_State)])

    def show_info(self, garden):
        pass

class Fell_Info(Info):
    def __init__(self):
        super().__init__()

    def update(self, garden):
        self.fruits.extend([fruit for tree in garden.trees for fruit in tree._fruits if isinstance(fruit.state, Overgrowth_State)])

    def show_info(self):
        pass

class Apple_Harvested_Info(Harvested_Info):
    def __init__(self):
        super().__init__()

    def update(self, garden):
        super().update(garden)
        self.fruits = [fruit for fruit in self.fruits if isinstance(fruit, Apple)]

    def show_info(self):
        fruitss = sum(1 for fruit in self.fruits if fruit.sort == 1)
        if fruitss > 0:
            print("Apple 1 sort Harvested - " + str(fruitss))
        fruitss = sum(1 for fruit in self.fruits if fruit.sort == 2)
        if fruitss > 0:
            print("Apple 2 sort Harvested - " + str(fruitss))
        fruitss = sum(1 for fruit in self.fruits if fruit.sort == 3)
        if fruitss > 0:
            print("Apple 3 sort Harvested - " + str(fruitss))

class Apple_Fell_Info(Fell_Info):
    def __init__(self):
        super().__init__()

    def update(self, garden):
        super().update(garden)
        self.fruits = [fruit for fruit in self.fruits if isinstance(fruit, Apple)]

    def show_info(self):
        fruitss = sum(1 for fruit in self.fruits if fruit.sort == 1)
        if fruitss > 0:
            print("Apple 1 sort Fell - " + str(fruitss))
        fruitss = sum(1 for fruit in self.fruits if fruit.sort == 2)
        if fruitss > 0:
            print("Apple 2 sort Fell - " + str(fruitss))
        fruitss = sum(1 for fruit in self.fruits if fruit.sort == 3)
        if fruitss > 0:
            print("Apple 3 sort Fell - " + str(fruitss))

class Cherry_Harvested_Info(Harvested_Info):
    def __init__(self):
        super().__init__()

    def update(self, garden):
        super().update(garden)
        self.fruits = [fruit for fruit in self.fruits if isinstance(fruit, Cherry)]

    def show_info(self):
        fruitss = sum(1 for fruit in self.fruits if fruit.sort == 1)
        if fruitss > 0:
            print("Cherry 1 sort Harvested - " + str(fruitss))
        fruitss = sum(1 for fruit in self.fruits if fruit.sort == 2)
        if fruitss > 0:
            print("Cherry 2 sort Harvested - " + str(fruitss))
        fruitss = sum(1 for fruit in self.fruits if fruit.sort == 3)
        if fruitss > 0:
            print("Cherry 3 sort Harvested - " + str(fruitss))

class Cherry_Fell_Info(Fell_Info):
    def __init__(self):
        super().__init__()

    def update(self, garden):
        super().update(garden)
        self.fruits = [fruit for fruit in self.fruits if isinstance(fruit, Cherry)]

    def show_info(self):
        fruitss = sum(1 for fruit in self.fruits if fruit.sort == 1)
        if fruitss > 0:
            print("Cherry 1 sort Fell - " + str(fruitss))
        fruitss = sum(1 for fruit in self.fruits if fruit.sort == 2)
        if fruitss > 0:
            print("Cherry 2 sort Fell - " + str(fruitss))
        fruitss = sum(1 for fruit in self.fruits if fruit.sort == 3)
        if fruitss > 0:
            print("Cherry 3 sort Fell - " + str(fruitss))

class Abstract_Fruits_Info(metaclass=abc.ABCMeta):
    
    def create_falling_info(self):
        pass

    def create_harvesting_info(self):
        pass

class Apple_Info(Abstract_Fruits_Info):
    
    def create_falling_info(self):
        return Apple_Fell_Info()
    
    def create_harvesting_info(self):
        return Apple_Harvested_Info()
    
class Cherry_Info(Abstract_Fruits_Info):
    def create_falling_info(self):
        return Cherry_Fell_Info()
    
    def create_harvesting_info(self):
        return Cherry_Harvested_Info()
    