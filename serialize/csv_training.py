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
