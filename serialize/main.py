from serialize.csv_training import csv_write, csv_read
from serialize.json_training import json_to_file, json_from_file
from serialize.pickle_training import pickle_write, pickle_read


def main():
    # PICKLE_TRAINING!
    # abc = ['milk', 'bread', 'butter']
    # pickle_write(abc)
    #
    # list_of_string = pickle_read()
    # print(list_of_string)

    # CSV_TRAINING!
    # users = [
    #     ("Marcin", "Najman", 82121699856),
    #     ("Jarosław", "Kot", 56011218822)
    # ]
    # csv_write(users)
    #
    # returned_users = csv_read()
    # print(returned_users)

    # JSON_TRAINING!
    # json_to_file()
    print(json_from_file())


if __name__ == '__main__':
    main()
