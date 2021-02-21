# Przygotuj aplikację pobierającą od użytkownika dowolny ciąg znaków i sprawdzającą
# czy wprowadzony numer seryjny jest poprawny. Numer seryjny składa się z 3 dużych
# liter, 5 cyfr, 1 małej litery i 1 dużej litery np. VSD43281fA.

import re


def exercise_6():
    print("Enter correct series number: ")
    value = input()

    expression = '[A-Z]{3}[0-9]{5}[a-z]{1}[A-Z]{1}'
    if re.fullmatch(expression, value):
        print("Series number is correct")
    else:
        print("Series number is incorrect")