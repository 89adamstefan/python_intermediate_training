from exception.exercises import case_1, case_2


def main():
    print("Start app")
    try:
        case_2("")
    except ValueError as ve:
        print(f'ValueError return {ve.args}')
    print("Finish")


if __name__ == "__main__":
    main()
