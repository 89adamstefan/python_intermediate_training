import pickle


def pickle_write(items: list):
    print("Pickle write start!")
    try:
        with open('./data.pickle', 'wb') as fd:
            pickle.dump(items, fd)
            print(pickle.dumps(items))
    except (IOError, Exception) as e:
        print(f'Exception while writing pickle format, info {e.args}')
    print("Finish!")

def pickle_read():
    print("Pickle read start!")
    string_list = []
    try:
        with open('./data.pickle', 'rb') as fd:
            string_list = pickle.load(fd)
    except (IOError, Exception) as e:
        print(f'Exception while reading pickle format, info {e.args}')
    print("Finish!")
    return string_list

