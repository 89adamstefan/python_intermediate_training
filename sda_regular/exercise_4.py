# Przygotuj aplikację pobierającą od użytkownika dowolny ciąg znaków i sprawdzającą
# czy wprowadzona wartość zawiera słowo "ala".

import re


def exercise_4():
    print("Enter some text with word 'ala': ")
    value = input()

    expression = '.*ala.*'
    if re.fullmatch(expression, value):
        print("Text have word 'ala'")
    else:
        print("Text doesnt have word 'ala'")
