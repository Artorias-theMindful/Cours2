import abc
import random
from tree import *
from garden import *
from fruit import *
class Gardener:
    def __init__(self, name):
        self.name = name
        self.gardens = []

    def create_garden(self):
        real_garden = Real_Garden()
        garden = Proxy_Garden(real_garden)
        self.gardens.append(garden)

    def plant_apple_tree(self, garden_index, sort):
        if 0 <= garden_index < len(self.gardens):
            tree_creator = Apple_Tree_Creator() 
            self.gardens[garden_index].plant(tree_creator.get_tree(sort))
            print("Apple planted!")
        else:
            print("Invalid garden index.")
    
    def plant_cherry_tree(self, garden_index, sort):
        if 0 <= garden_index < len(self.gardens):
            tree_creator = Cherry_Tree_Creator()
            self.gardens[garden_index].plant(tree_creator.get_tree(sort))
            print("Cherry planted!")
        else:
            print("Invalid garden index.")

    def water_garden(self, garden_index):
        if 0 <= garden_index < len(self.gardens):
            garden = self.gardens[garden_index]
            garden.notify("water")
        else:
            print("Invalid garden index.")

    def destroy_pests(self, garden_index):
        if 0 <= garden_index < len(self.gardens):
            garden = self.gardens[garden_index]
            garden.notify("clean")
        else:
            print("Invalid garden index.")

    def harvest_fruits(self, garden_index):
        if 0 <= garden_index < len(self.gardens):
            garden = self.gardens[garden_index]
            garden.harvested()
        else:
            print("Invalid garden index.")