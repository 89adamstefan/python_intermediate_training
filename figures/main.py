from figures.figures_entities import *


def main():
    circle1 = Circle(5)
    circle2 = Circle(10)
    circle3 = Circle(15)
    triangle1 = Triangle(15, 5)
    triangle2 = Triangle(20, 10)
    triangle3 = Triangle(10, 5)
    rectangle1 = Rectangle(35, 5)
    rectangle2 = Rectangle(45, 5)
    rectangle3 = Rectangle(50, 5)

    print(circle1.get_area())
    print(triangle2.get_area())
    print(rectangle3.get_area())

    # area = Figure.count_area([triangle3, circle3, rectangle2])
    # print(area)

    area = count_area_func(triangle2, circle1, rectangle3)
    print(area)

    result = Figure.check_area(100.00, [circle1, triangle1, rectangle1])
    print(result)
    print(Figure.count_area([circle1, triangle1, rectangle1]))



if __name__ == "__main__":
    main()