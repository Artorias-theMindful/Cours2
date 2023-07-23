import abc
import random
import copy
class Fruit(metaclass=abc.ABCMeta):
    def __init__(self, sort):
        self.state = Normal_State(self)
        self.readiness = 0
        self.sort = sort

    def set_state(self, state):
        self.state = state

    def increase_readiness(self):
        self.readiness += self.speed

class Apple(Fruit):
    def __init__(self, sort):
        super().__init__(sort)
        self.speed = 15

class Cherry(Fruit):
    def __init__(self, sort):
        super().__init__(sort)
        self.speed = 30
        

class State(metaclass=abc.ABCMeta):

    def __init__(self, fruit):
        self._fruit = fruit
    def update(self, event):
        pass
    
class Normal_State(State):

    def __init__(self, fruit):
        super().__init__(fruit)

    def update(self, event):
        if event == "water":
            self._fruit.increase_readiness()
            if self._fruit.readiness > 80:
                self._fruit.set_state(Ready_State(self._fruit))
            if random.random() < 0.2:
                self._fruit.set_state(Poisoned_State(self._fruit))
    
class Poisoned_State(State):

    def __init__(self, fruit):
        super().__init__(fruit)
    
    def update(self, event):
        if event == "clean":
            if self._fruit.readiness < 80:
                self._fruit.set_state(Normal_State(self._fruit))
            else:
                self._fruit.set_state(Ready_State(self._fruit))

class Ready_State(State):
    
    def __init__(self, fruit):
        super().__init__(fruit)

    def update(self, event):
        if event == "water":
            self._fruit.increase_readiness()
            if self._fruit.readiness > 100:
                self._fruit.set_state(Overgrowth_State(self._fruit))

class Overgrowth_State(State):
    def __init__(self, fruit):
        super().__init__(fruit)