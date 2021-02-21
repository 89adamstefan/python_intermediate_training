# Przygotuj aplikację pobierającą od użytkownika dowolny ciąg znaków i sprawdzającą
# czy wprowadzona wartość jest poprawnym loginem użytkownika. Za poprawny login
# uważamy tekst zawierający małe i duże litery oraz cyfry. Jego minimalna długość to
# 8 a maksymalna 16 znaków.
import re


def exercise_3():
    print("Write user login here: ")
    value = input()

    expression = '[0-9a-zA-Z]{8,16}'
    if re.fullmatch(expression, value):
        print("User login is correct")
    else:
        print("User login is incorrect")
