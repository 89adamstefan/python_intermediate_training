from sda_exercises_oop_1.cat import Cat


def main():
    cat_object = Cat("Mruczek")
    cat_object2 = Cat("Rudy")
    cat_object3 = Cat("Murzyn")
    cat_object4 = Cat("Jarek", "***** ***")

    # cats = [cat_object, cat_object2, cat_object3, cat_object4]
    cats = []

    cats.append(cat_object)
    cats.append(cat_object2)
    cats.append(cat_object3)
    cats.append(cat_object4)

    # for cat in cats:
    #     sound = cat.make_sound()
    #     print(sound)

    cat_object.eat_mouse()
    cat_object.eat_mouse()
    cat_object.eat_mouse()
    print("Now next cat was eaten mouse!")
    cat_object2.eat_mouse()



if __name__ == "__main__":
    main()
