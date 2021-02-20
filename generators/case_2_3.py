def numbers_creator(n):
    list_of_numbers = []
    for number in range(n):
        list_of_numbers.append(number)
    return list_of_numbers


def iterator_ex_2(n):
    print("Exercise 2")
    import sys
    result_list = numbers_creator(n)
    print(f'Size of list in bytes: {sys.getsizeof(result_list)}')
    result = sum(result_list)
    print(f'Size of one number in bytes: {sys.getsizeof(result)}')
    print(result)
