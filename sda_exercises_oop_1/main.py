from sda_exercises_oop_1.cat import Cat
from sda_exercises_oop_1.dog import Dog


def main():
    cat_object = Cat("Mruczek")
    cat_object2 = Cat("Rudy")
    cat_object3 = Cat("Murzyn")
    cat_object4 = Cat("Jarek", "***** ***")
    dog_object = Dog("Burek")
    dog_object2 = Dog("Pimpek")
    dog_object3 = Dog("Lessie")

    # print(dog_object.make_sound)

    # cats = [cat_object, cat_object2, cat_object3, cat_object4]
    animals = []

    animals.append(cat_object)
    animals.append(cat_object2)
    animals.append(cat_object3)
    animals.append(cat_object4)
    animals.append(dog_object)
    animals.append(dog_object2)
    animals.append(dog_object3)

    for animal in animals:
        sound = animal.make_sound()
        print(sound)

    # cat_object.eat_mouse()
    # cat_object.eat_mouse()
    # cat_object.eat_mouse()
    # print("Now the next cat will eat the mouse!")
    # cat_object2.eat_mouse()





if __name__ == "__main__":
    main()
