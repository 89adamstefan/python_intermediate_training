def main():
    a, b = print_helo_world(1, 2)
    print(f'In main {a} {b}')


def wrap_before_and_after(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result

    return wrapper


@wrap_before_and_after
def print_helo_world(a, b):
    print("Hello World!")
    print(f'{a, b}')
    return a, b


if __name__ == '__main__':
    main()