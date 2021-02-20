class Iterable:
    def __init__(self, amount):
        self.amount = amount
        self.value_creator = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.value_creator >= self.amount -1:
            raise StopIteration
        self.value_creator += 1
        return self.value_creator

def iterator_ex_3(n):
    print("Exercise 2")
    import sys
    iterator = Iterable(n)
    print(f'Size of list in bytes: {sys.getsizeof(iterator)}')
    result = sum(iterator)
    print(f'Size of one number in bytes: {sys.getsizeof(result)}')
    print(result)