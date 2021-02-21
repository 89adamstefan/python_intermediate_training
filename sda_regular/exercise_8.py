# Przygotuj wyrażenie regularne sprawdzające czy numer faktury VAT jest poprawny.
# Przykładowy numer faktury to "FV/1024/02/2018", gdzie
# FV - stały wpis
# / - stały znak rozdzielający sekcje
# 1024 - kolejny numer faktury w danym miesiącu. Numer rozpoczyna się od 1
# / - stały znak rozdzielający sekcje
# 02 - numer miesiąca w danym roku kalendarzowym
# / - stały znak rozdzielający sekcje
# 2018 - rok

import re


def exercise_8():
    print("Please provide invoice number: ")
    value = input()

    expression = '[FV/[1]+[0-9]{3}/[0-9]{2}/[0-9]{4}'
    if re.fullmatch(expression, value):
        print("Invoice number is correct")
    else:
        print("Invoice number is incorrect")
