from figures.figures_entities import *

def main():
    circle = Circle(5)
    traingle = Triangle(15, 5)
    rectangle = Rectangle(35, 5)

    print(circle.get_area())
    print(traingle.get_area())
    print(rectangle.get_area())








if __name__ == "__main__":
    main()