


def translate(sentence):
    words = {'איז': 'is', 'די': 'the', 'אין': 'in', 'קאץ': 'cat', 'שטוב': 'house', 'אף': 'on'}
    return list(words[it] for it in sentence.split())


print(*translate('די קאץ איז אין די קאץ אף די שטוב'))


def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def first_prime_over(n):
    iterator = (i for i in range(n+1,n*4) if is_prime(i))
    return iterator.__next__()


print(first_prime_over(1000000))