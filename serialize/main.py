from serialize.csv_training import csv_write
from serialize.pickle_training import pickle_write, pickle_read


def main():
    # PICKLE_TRAINING!
    # abc = ['milk', 'bread', 'butter']
    # pickle_write(abc)
    #
    # list_of_string = pickle_read()
    # print(list_of_string)

    # CSV_TRAINING!
    users = [
        ("Marcin", "Najman", 82121699856),
        ("Jarosław", "Kot", 56011218822)
    ]
    csv_write(users)


if __name__ == '__main__':
    main()
