import re


def exercise_2():
    print("Write postal code here: ")
    value = input()

    expression = '[0-9]{2}-[0-9]{3}'
    if re.fullmatch(expression, value):
        print("Postal code is correct")
    else:
        print("Postal code is incorrect")
