import abc
import random
from viewer import *

class Garden(metaclass=abc.ABCMeta):
    def __init__(self):
        self.trees = []
        apple_info = Apple_Info()
        cherry_info = Cherry_Info()
        self.apple_harvested = apple_info.create_harvesting_info()
        self.apple_fell = apple_info.create_falling_info()
        self.cherry_harvested = cherry_info.create_harvesting_info()
        self.cherry_fell = cherry_info.create_falling_info()
    def notify(self, event):
        pass
    def harvested(self):
        pass
    def plant(self, tree):
        pass

class Real_Garden(Garden):
    def __init__(self):
        super().__init__()

    def notify(self, event):
        for tree in self.trees:
            tree.notify(event)
            self.apple_fell.update(self)
            self.cherry_fell.update(self)
            tree.drop_fruits()
            tree.make_fruits()

    def harvested(self):
        self.apple_harvested.update(self)
        self.cherry_harvested.update(self)
        for tree in self.trees:
            tree.harvested()
        self.apple_harvested.show_info()
        self.cherry_harvested.show_info()
    
    def plant(self, tree):
        self.trees.append(tree)

class Proxy_Garden(Garden):
    def __init__(self, garden):
        super().__init__()
        self.garden = garden
    
    def notify(self, event):
        if len(self.garden.trees) == 0:
            print("Plant a tree first")
        else:
            self.garden.notify(event)
            print(event + "ing successful!")
    
    def harvested(self):
        if len(self.garden.trees) == 0:
            print("Plant a tree first")
        else:
            self.garden.harvested()
            print("Harvesting successful!")
    
    def plant(self, tree):
        self.garden.plant(tree)
    
    def get_trees(self):
        return self.garden.trees
    
    def get_apple_harvested(self):
        return self.garden.apple_harvested
    
    def get_apple_fell(self):
        return self.garden.apple_fell
    
    def get_cherry_harvested(self):
        return self.garden.cherry_harvested
    
    def get_cherry_fell(self):
        return self.garden.cherry_fell
