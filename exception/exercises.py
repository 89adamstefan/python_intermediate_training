import sys


def case_1():
    list_of_numbers = [1, 5, 8, 10, 21]
    print("Case_1 before")
    #  first example
    try:
        result = list_of_numbers[6]
    except IndexError as ie:
        print(f'Exception cought {ie.args}')
    except Exception as exp:
        print(f'Exception cought {exp.args}')
    print("Case_1 after")
    #  second example
    try:
        result = list_of_numbers[6]
    except (IndexError, Exception) as e:
        print(f'Exception cought by tuple {e.args}')


def case_2(name: str):
    if len(name) <= 0:
        raise ValueError('String is empty!')
    print(f'Given name is: {name}')


def case_3(number: int, divisor: int) -> float:
    result = 0
    try:
        result = number / divisor
    except ZeroDivisionError as zde:
        print("The divisor value cannot be zero")
        result = sys.float_info.max
        # result = float(sys.maxsize)
    return result


def case_4(dictionary: dict):
    key = 'items'
    try:
        items: list = dictionary[key]
        for item in items:
            print(item)
    except KeyError as ke:
        print(f'Key {key} not found, more information {ke.args}')

def case_4_v2(dictionary: dict):
    key = 'items'
    items: list = dictionary.get(key, [])
    for item in items:
        print(item)
    if not items:
        print("Key does not exist or list is empty")

def case_6():
    raise NotImplementedError("Sovled in future")
