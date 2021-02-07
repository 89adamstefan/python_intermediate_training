from serialize.pickle_training import pickle_write, pickle_read


def main():
    abc = ['milk', 'bread', 'butter']
    pickle_write(abc)

    list_of_string = pickle_read()
    print(list_of_string)


if __name__ == '__main__':
    main()
