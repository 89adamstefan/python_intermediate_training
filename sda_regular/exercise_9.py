# Przygotuj aplikację pobierającą od użytkownika dowolny tekst. Wprowadzony tekst
# powinien zostać podzielony na słowa korzystając z metody split, a następnie
# program powinien wyświetlić statystyki wpisanego przez użytkownika tekstu.
# Ilość słów: <ilość_słów>
# Ilość wprowadzonych znaków: <ilość_znaków>
# Średnia długość wprowadzonego słowa: <ilość_znaków>
# Najdłuższe słowo: <ilość_znaków>
# Najkrótsze słowo: <ilość_znaków>
# Do testów użyj podanego zdania:
# “Drogi Marszałku, Wysoka Izbo. PKB rośnie. Z pełną odpowiedzialnością mogę
# stwierdzić iż realizacja określonych zadań stanowionych przez organizację. Dalszy
# rozwój jest ważne zadanie w większym stopniu tworzenie odpowiednich warunków
# aktywizacji. Często niezauważanym szczegółem jest to, że zakres i rozwijanie
# struktur pociąga za najważniejszy punkt naszych działań obierzemy praktykę, nie zaś
# teorię, okazuje się jasne.”

import re


def exercise_9():
    text = """ Drogi Marszałku, Wysoka Izbo. PKB rośnie. Z pełną odpowiedzialnością mogę
    stwierdzić iż realizacja określonych zadań stanowionych przez organizację.
    Dalszy rozwój jest ważne zadanie w większym stopniu tworzenie odpowiednich
    warunków aktywizacji. Często niezauważanym szczegółem jest to, że zakres
    i rozwijanie struktur pociąga za najważniejszy punkt naszych działań
    obierzemy praktykę, nie zaś teorię, okazuje się jasne
    """

    empty_text = ''

    words_number = text.split()
    # print(words_number)
    print(f'Words number: {len(words_number)}')

    char_number = re.split(empty_text, text)
    # print(char_number)
    print(f'Characters number: {len(char_number)}')

    average_operation = [len(char_number) for char_number in words_number]
    # print(average_operation)
    average = sum(average_operation)/len(average_operation)
    print(f'The average word length is: {average:.2f}')

    max_word = [len(char_number) for char_number in words_number]
    print(f'The longest number of characters in a word: {max(max_word)}')

    min_word = [len(char_number) for char_number in words_number]
    print(f'The shortest number of characters in a word: {min(min_word)}')
