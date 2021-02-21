# Numer seryjny oprogramowania ma postać "CFG&Y-TYH67-GH56T-UIO99-RY4RT",
# gdzie każdy blok może składać się z dużych liter lub cyfr. Bloki oddzielone są
# myślnikami "-". W numerze występuje dokładnie 5 bloków z wartościami. Przygotuj
# wyrażenie regularne sprawdzające numer seryjny.

import re


def exercise_7():
    print("Please provide correct software serial number: ")
    value = input()

    expression = '[0-9A-Z%$&@#]{5}\-[0-9A-Z%$&@#]{5}\-[0-9A-Z%$&@#]{5}\-[0-9A-Z%$&@#]{5}\-[0-9A-Z%$&@#]{5}'
    if re.fullmatch(expression, value):
        print("Serial number is correct")
    else:
        print("Serial number is incorrect")