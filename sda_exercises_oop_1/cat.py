class Cat:
    def __init__(self, name: str, sound='Meow!'):
        self.name = name
        self.sound = sound

    def make_sound(self) -> str:
        return f'Name is {self.name} and make sound {self.sound}'
