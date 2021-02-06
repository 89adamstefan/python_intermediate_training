from sda_exercises_oop_1.animal import Animal
from sda_exercises_oop_1.movable import Movable


class Cat(Movable, Animal):
    def move(self) -> str:
        return "Idzie"

    def __init__(self, name: str, sound='Meow!', eaten_mouse=0):
        Animal.__init__(self, name)
        self.sound = sound
        self.eaten_mouse = eaten_mouse

    def make_sound(self) -> str:
        return f'Name is {self.name} ,make sound {self.sound}'

    def eat_mouse(self) -> int:
        self.eaten_mouse += 1
        print(f'Im eat {self.eaten_mouse} mouses, yeah!')
        return self.eaten_mouse

    def drink(self):
        print("Cat drink water")

