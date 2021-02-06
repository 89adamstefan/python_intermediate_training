from sda_exercises_oop_1.animal import Animal
from sda_exercises_oop_1.cat import Cat
from sda_exercises_oop_1.dog import Dog


class Vet:

    @staticmethod
    def say_cat_hello(cat: Cat) -> str:
        return f'Hello {cat.name}'

    @staticmethod
    def say_dog_hello(dog: Dog):
        print(f'Hello {dog.name}')

    def say_hello(self, animal: Animal):
        print(f'Hello {animal.name}')