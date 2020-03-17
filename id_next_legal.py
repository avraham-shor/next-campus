def check_id_valid(id_number):
    """
    The function get a id_number param and checks if the id is valid.
    :param id_number:
    :return: True if  the id is valid, False if the id is not valid.
    """
    if len(str(int(id_number))) < 9:
        """:raises a ValueError if the id is missing digits and is less than 9 digits"""
        raise ValueError('The id missing numbers got only 9 numbers')
    if len(str(int(id_number))) > 9:
        """:raises a ValueError if the id has too many digits and is more than 9 digits"""
        raise ValueError('The id takes only 9 numbers but more were given')
    list_id = [int(num) if index % 2 == 0 else int(num) * 2 for index, num in enumerate(str(id_number))]
    list_id2 = [num if num < 10 else int(str(num)[0]) + int(str(num)[1]) for num in list_id]
    return sum(list_id2) == 40


class IDIterator:
    """
    The iterator class get a id param,
    returns: the next valid id's
    """

    def __init__(self, _id):
        self._id = _id - 1

    def __iter__(self):
        return self

    def __next__(self):
        self._id += 1
        while not check_id_valid(self._id):
            self._id += 1
        return self._id


def id_generator(id_number):
    """
    The generator get a id param and returns the next valid id's.
    :param id_number:
    :return: the next valid id's.
    """
    while True:
        id_number += 1
        if not check_id_valid(id_number - 1):
            id_number += 1
        yield id_number


def main():
    """
    calls to class IDIterator and to function id_generator with param-id '123456780'.
    :output: 10 next valid id's.
    """
    id_itertator = IDIterator(123456780)
    for _ in range(10):
        print(next(id_itertator))

    id_gen = id_generator(123456780)
    print()
    for _ in range(10):
        print(next(id_gen))


if __name__ == '__main__':
    main()
