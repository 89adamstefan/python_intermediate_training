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