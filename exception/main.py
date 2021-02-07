from exception.exercises import case_1, case_2, case_3


def main():
    print("Start app")
    # try:
    #     case_2("")
    # except ValueError as ve:
    #     print(f'ValueError return {ve.args}')

    result = case_3(10, 0)
    print(result)


    print("Finish")


if __name__ == "__main__":
    main()
