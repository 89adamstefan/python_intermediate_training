from sda_exercises_oop_1.animal import Animal


class Dog(Animal):
    def drink(self):
        print("Dog drink vodka")

    def __init__(self, name: str, sound='Woof! Woof!'):
        super().__init__(name)
        self.sound = sound

    def make_sound(self) -> str:
        return f'Name is {self.name} ,make sound {self.sound}'
