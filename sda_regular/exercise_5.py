# Przygotuj aplikację pobierającą od użytkownika dowolny ciąg znaków i sprawdzjącą
# czy wprowadzona data jest poprawna. Za poprawną datę uważamy zapis w postaci
# "10.02.2018r.". Na potrzeby zadania nie weryfikujemy wartości dnia miesiąca. 45 to
# też poprawna wartość.


import re


def exercise_5():
    print("Enter some date with format dd.mm.yyyy: ")
    value = input()

    expression = '[0-9]{2}\.[0-9]{2}\.[0-9]{4}'
    if re.fullmatch(expression, value):
        print("Date is correct")
    else:
        print("Date is incorrect")
