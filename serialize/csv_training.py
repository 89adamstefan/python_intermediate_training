import csv


def csv_write(users: list):
    print("CSV write start!")
    try:
        with open('./data.csv', 'w') as fd:
            writer = csv.writer(fd)
            for user_tuple in users:
                writer.writerow(user_tuple)

    except (IOError, Exception) as e:
        print(f'Exception while writing csv format, info {e.args}')
    print("Finish!")


def csv_read():
    users = []
    print("CSV read start!")
    try:
        with open('./data.csv', 'r') as fd:
            reader = csv.reader(fd)
            for row in reader:
                if row:
                    users.append(row)

    except (IOError, Exception) as e:
        print(f'Exception while reading csv format, info {e.args}')
    print("Finish!")
    return users
