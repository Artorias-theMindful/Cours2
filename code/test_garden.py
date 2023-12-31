import unittest
import interface
import json
import os
from gardener import *
from garden import *
from fruit import *
from tree import *
class TestGarden(unittest.TestCase):

    def test_save_gardener(self):
        gardener_to_save = Gardener("Artem")
        interface.save_gardener(gardener_to_save)
        data = interface.get_data()
        self.assertEqual(str(data), "{\'gardener\': {\'name\': \'Artem\'}, \'gardens\': []}")
    
    def test_save_garden(self):
        gardener_to_save = Gardener("Artem")
        gardener_to_save.create_garden()
        interface.save_gardener(gardener_to_save)
        data = interface.get_data()
        string = "{\"gardener\": {\"name\": \"Artem\"}, \"gardens\": [{\"trees\": [], \"apple_harvested\": [], \"apple_fell\": [], \"cherry_harvested\": [], \"cherry_fell\": []}]}"
        string = string.replace('"', "'")
        self.assertEqual(str(data), string)

    def test_plant_trees(self):
        gardener = Gardener("Artem")
        gardener.create_garden()
        gardener.plant_apple_tree(0, 1)
        gardener.plant_cherry_tree(0, 3)
        self.assertIsInstance(gardener.gardens[0].garden.trees[0], Apple_Tree)
        self.assertIsInstance(gardener.gardens[0].garden.trees[1], Cherry_Tree)
        self.assertEqual(gardener.gardens[0].garden.trees[0]._sort, 1)
        self.assertEqual(gardener.gardens[0].garden.trees[1]._sort, 3)
    
    def test_water(self):
        gardener = Gardener("Artem")
        gardener.create_garden()
        gardener.plant_apple_tree(0, 3)
        gardener.water_garden(0)
        gardener.water_garden(0)
        gardener.water_garden(0)
        gardener.water_garden(0)
        gardener.water_garden(0)
        gardener.water_garden(0)
        gardener.water_garden(0)
        gardener.water_garden(0)
        gardener.water_garden(0)
        gardener.water_garden(0)
        gardener.water_garden(0)
        gardener.water_garden(0)
        self.assertIsInstance(gardener.gardens[0].garden.trees[0]._fruits[0].state, Poisoned_State)
        self.assertEqual(gardener.gardens[0].garden.trees[0]._fruits[0].readiness > 0, True)
    
    def test_clean(self):
        gardener = Gardener("Artem")
        gardener.create_garden()
        gardener.plant_apple_tree(0, 3)
        gardener.water_garden(0)
        gardener.water_garden(0)
        gardener.water_garden(0)
        gardener.water_garden(0)
        gardener.water_garden(0)
        gardener.water_garden(0)
        gardener.water_garden(0)
        gardener.water_garden(0)
        gardener.water_garden(0)
        gardener.water_garden(0)
        gardener.water_garden(0)
        gardener.water_garden(0)
        gardener.destroy_pests(0)
        for i in gardener.gardens[0].garden.trees[0]._fruits:
            self.assertEqual(i.state != Poisoned_State, True, i.state)
    
    def test_harvest(self):
        gardener = Gardener("Artem")
        gardener.create_garden()
        gardener.plant_apple_tree(0, 3)
        for i in range(0, 15):
            gardener.water_garden(0)
            gardener.destroy_pests(0)
        gardener.harvest_fruits(0)
        self.assertEqual(len(gardener.gardens[0].garden.apple_harvested.fruits) > 0, True)

    def test_fall(self):
        gardener = Gardener("Artem")
        gardener.create_garden()
        gardener.plant_apple_tree(0, 3)
        for i in range(0, 15):
            gardener.water_garden(0)
            gardener.destroy_pests(0)
        self.assertEqual(len(gardener.gardens[0].garden.apple_fell.fruits) > 0, True)

if __name__ == '__main__':
    unittest.main()


