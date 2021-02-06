import pytest
from figures.figures_entities import Figure, Circle, Triangle, Rectangle, count_area_func


def test_count_area():
    #  given
    circle1 = Circle(1)
    triangle1 = Triangle(2, 1)
    rectangle1 = Rectangle(2, 2)
    #  when
    result = Figure.count_area([circle1, triangle1, rectangle1])
    #  then
    assert result == 8.14

def test_check_area():
    #  given
    circle1 = Circle(1)
    triangle1 = Triangle(2, 1)
    rectangle1 = Rectangle(2, 2)
    area = count_area_func(triangle1, circle1, rectangle1)
    #  when
    result = Figure.check_area(area, [circle1, triangle1, rectangle1])
    #  then
    assert result <= 15