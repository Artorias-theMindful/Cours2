from gardener import *
from garden import *
from fruit import *
from tree import *
import os
import json
def get_data():
    try:
        with open('data.json', 'r') as openfile:
            return json.load(openfile)
    except FileNotFoundError:
        return None


data = get_data()
if data is None:
    gardener = Gardener(input("What is your name, gardener? "))
else:
    gardener_data = data["gardener"]
    gardener = Gardener(gardener_data["name"])
    gardens_data = data["gardens"]
    for garden_data in gardens_data:
        trees_data = garden_data["trees"]
        apple_harvested = garden_data["apple_harvested"]
        apple_fell = garden_data["apple_fell"]
        cherry_harvested = garden_data["cherry_harvested"]
        cherry_fell = garden_data["cherry_fell"]
        real_garden = Real_Garden()
        garden = Proxy_Garden(real_garden)
        for apple_harvested_ in apple_harvested:
            apple_harvested_sort = apple_harvested_["sort"]
            apple_harvested_readiness = apple_harvested_["readiness"]
            apple_harvested__ = Apple(apple_harvested_sort)
            apple_harvested__.readiness = apple_harvested_readiness
            apple_harvested__.state = Ready_State(apple_harvested__)
            garden.get_apple_harvested().fruits.append(apple_harvested__)
        for apple_fell_ in apple_fell:
            apple_fell_sort = apple_fell_["sort"]
            apple_fell_readiness = apple_fell_["readiness"]
            apple_fell__ = Apple(apple_fell_sort)
            apple_fell__.readiness = apple_fell_readiness
            apple_fell__.state = Overgrowth_State(apple_fell__)
            garden.get_apple_fell().fruits.append(apple_fell__)
        for cherry_harvested_ in cherry_harvested:
            cherry_harvested_sort = cherry_harvested_["sort"]
            cherry_harvested_readiness = cherry_harvested_["readiness"]
            cherry_harvested__ = Cherry(cherry_harvested_sort)
            cherry_harvested__.readiness = cherry_harvested_readiness
            cherry_harvested__.state = Ready_State(cherry_harvested__)
            garden.get_cherry_harvested().fruits.append(cherry_harvested__)
        for cherry_fell_ in cherry_fell:
            cherry_fell_sort = cherry_fell_["sort"]
            cherry_fell_readiness = cherry_fell_["readiness"]
            cherry_fell__ = Cherry(cherry_fell_sort)
            cherry_fell__.readiness = cherry_fell_readiness
            cherry_fell__.state = Overgrowth_State(cherry_fell__)
            garden.get_cherry_fell().fruits.append(cherry_fell__)
        for tree_data in trees_data:
            sort = tree_data["sort"]
            max_fruits = tree_data["max_fruits"]
            speed = tree_data["speed"]
            tree_type = tree_data["type"]
            if tree_type == "apple":
                tree = Apple_Tree(sort, max_fruits, speed)
            elif tree_type == "cherry":
                tree = Cherry_Tree(sort, max_fruits, speed)
            
            fruits_data = tree_data["fruits"]

            for fruit_data in fruits_data:
                fruit_sort = fruit_data["sort"]
                fruit_type = fruit_data["type"]
                fruit_readiness = fruit_data["readiness"]
                fruit_state = fruit_data["state"]
                tree_type = tree_data["type"]
                if fruit_type == "apple":
                    fruit = Apple(fruit_sort)
                elif fruit_type == "cherry":
                    fruit = Cherry(fruit_sort)
                fruit.readiness = fruit_readiness
                if fruit_state == "normal":
                    fruit.state = Normal_State(fruit)
                if fruit_state == "poisoned":
                    fruit.state = Poisoned_State(fruit)
                if fruit_state == "ready":
                    fruit_state = Ready_State(fruit)
                if fruit_state == "overgrowth":
                    fruit_state = Overgrowth_State(fruit)
                tree._fruits.append(fruit)
            garden.get_trees().append(tree)
        gardener.gardens.append(garden)
print("Welcome to the garden!")
while True:
    print("1 - show gardens and trees")
    print("2 - set up a garden")
    print("3 - visit a sertain garden")
    print("4 - save and leave")
    command = input()
    if command == "1":
        for g in gardener.gardens:
            print(str(gardener.gardens.index(g) + 1) + " garden:")
            for t in g.get_trees():
                if isinstance(t, Apple_Tree):
                    print("    Apple tree")
                    print("        sort - " + str(t._sort))
                    print("        speed - " + str(t._speed))
                    print("        max fruits - " + str(t._max_fruits))
                if isinstance(t, Cherry_Tree):
                    print("    Cherry tree")
                    print("        sort - " + str(t._sort))
                    print("        speed - " + str(t._speed))
                    print("        max fruits - " + str(t._max_fruits))
    if command == "2":
        gardener.create_garden()
        print("New empty garden was created")
    if command == "3":
        index = int(input("Choose a garden to visit: ")) - 1
        if 0 <= index < len(gardener.gardens):
            for t in gardener.gardens[index - 1].get_trees():
                if isinstance(t, Apple_Tree):
                    print("    Apple tree")
                    print("        sort - " + str(t._sort))
                    print("        speed - " + str(t._speed))
                    print("        max fruits - " + str(t._max_fruits))
                if isinstance(t, Cherry_Tree):
                    print("    Cherry tree")
                    print("        sort - " + str(t._sort))
                    print("        speed - " + str(t._speed))
                    print("        max fruits - " + str(t._max_fruits))
        else:
            print("Invalid index")
            continue
        while True:
            print("Choose an option:")
            print("1 - fruits harvested in this garden")
            print("2 - plant a tree in this garden")
            print("3 - clean trees")
            print("4 - water trees")
            print("5 - harvest fruits")
            print("6 - fruits fallen in this garden")
            print("7 - exit from a garden")
            command1 = int(input())
            if command1 == 1:
                gardener.gardens[index].get_apple_harvested().show_info()
                gardener.gardens[index].get_cherry_harvested().show_info()
            if command1 == 2:
                tree_to_plant = input("What type? ")
                if tree_to_plant == "apple":
                    sort = int(input("What sort (from 1 to 3)? "))
                    if 0 < sort < 4:
                        gardener.plant_apple_tree(index, sort)
                    else:
                        print("inapropriate sort")
                        continue
                elif tree_to_plant == "cherry":
                    sort = int(input("What sort (from 1 to 3)? "))
                    if 0 < sort < 4:
                        gardener.plant_cherry_tree(index, sort)
                    else:
                        print("Inapropriate sort")
                        continue
            if command1 == 3:
                gardener.destroy_pests(index)
            if command1 == 4:
                gardener.water_garden(index)
            if command1 == 5:
                gardener.harvest_fruits(index)
            if command1 == 6:
                gardener.gardens[index].get_apple_fell().show_info()
                gardener.gardens[index].get_cherry_fell().show_info()
            if command1 == 7:
                break
    if command == "4":
        data = {
            "gardener" : {
                "name" : gardener.name
            },
            "gardens": []
        }
        for garden in gardener.gardens:
            garden_data = {
                "trees": [],
                "apple_harvested": [],
                "apple_fell": [],
                "cherry_harvested": [],
                "cherry_fell": [],
            }
            for apple_harvested in garden.get_apple_harvested().fruits:
                apple_harvested_ = {
                    "readiness": apple_harvested.readiness,
                    "sort": apple_harvested.sort 
                }
                garden_data["apple_harvested"].append(apple_harvested_)
            for apple_fell in garden.get_apple_fell().fruits:
                apple_fell_ = {
                    "readiness": apple_fell.readiness,
                    "sort": apple_fell.sort 
                }
                garden_data["apple_fell"].append(apple_fell_)
            for cherry_harvested in garden.get_cherry_harvested().fruits:
                cherry_harvested_ = {
                    "readiness": cherry_harvested.readiness,
                    "sort": cherry_harvested.sort 
                }
                garden_data["cherry_harvested"].append(cherry_harvested_)
            for cherry_fell in garden.get_cherry_fell().fruits:
                cherry_fell_ = {
                    "readiness": cherry_fell.readiness,
                    "sort": cherry_fell.sort 
                }
                garden_data["cherry_fell"].append(cherry_fell_)
            
            for tree in garden.get_trees():
                if isinstance(tree, Apple_Tree):
                    typ = "apple"
                if isinstance(tree, Cherry_Tree):
                    typ = "cherry"
                tree_data = {
                    "sort" : tree._sort,
                    "type" : typ,
                    "max_fruits": tree._max_fruits,
                    "speed": tree._speed,
                    "fruits": []
                }
                for fruit in tree._fruits:
                    if isinstance(fruit, Apple):
                        fruit_type = "apple"
                    if isinstance(fruit, Cherry):
                        fruit_type = "cherry"
                    if isinstance(fruit.state, Normal_State):
                        fruit_state = "normal"
                    if isinstance(fruit.state, Poisoned_State):
                        fruit_state = "poisoned"
                    if isinstance(fruit.state, Ready_State):
                        fruit_state = "ready"
                    if isinstance(fruit.state, Overgrowth_State):
                        fruit_state = "overgrowth"
                    fruit_data = {
                        "sort": fruit.sort,
                        "type": fruit_type,
                        "readiness": fruit.readiness,
                        "state" : fruit_state
                    }
                    tree_data["fruits"].append(fruit_data)
                garden_data["trees"].append(tree_data)
            data["gardens"].append(garden_data)
        with open("data.json", "w") as file:
            json.dump(data, file)
        break
