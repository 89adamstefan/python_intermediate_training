# Przygotuj aplikację pobierającą od użytkownika dowolny ciąg znaków i sprawdzającą
# czy wprowadzony numer seryjny jest poprawny. Numer seryjny składa się z 3 dużych
# liter, 5 cyfr, 1 małej litery i 1 dużej litery np. VSD43281fA.

import re


def exercise_5():
    print("Enter some date with format dd.mm.yyyy: ")
    value = input()

    expression = '[0-9]{2}\.[0-9]{2}\.[0-9]{4}'
    if re.fullmatch(expression, value):
        print("Date is correct")
    else:
        print("Date is incorrect")