from itertools import combinations

dollars = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]


def hundred_dollars():
    account = 0
    for i in range(len(dollars)):
        list_dollars = set(combinations(dollars, i))
        for dollar in list_dollars:
            if sum(dollar) == 100:
                print(dollar)
                account += 1
    return account


# numbers = iter(list(range(1, 101)))
# for i in numbers:
#     next(numbers)
#     next(numbers)
#     print(i)
# print(dir(numbers))
print(hundred_dollars())
