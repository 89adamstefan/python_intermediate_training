class Dog:
    def __init__(self, name: str, sound='Woof! Woof!'):
        self.name = name
        self.sound = sound

    def make_sound(self) -> str:
        return f'Name is {self.name} ,make sound {self.sound}'