from sda_exercises_oop_1.car import Car
from sda_exercises_oop_1.cat import Cat
from sda_exercises_oop_1.dog import Dog
from sda_exercises_oop_1.vet import Vet


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

    # car = Car()
    # print(car.move())
    #
    cat = Cat("Mruczek")
    # print(cat.move())
    dog = Dog("Burek")

    print(Vet.say_cat_hello(cat))
    Vet.say_dog_hello(dog)

    vet = Vet()
    vet.say_dog_hello(dog)
    vet.say_hello(cat)




if __name__ == "__main__":
    main()