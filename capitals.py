

# with open("capitals.txt") as file:
#     single_line_gen = (line for line in file)
#     countries_and_capitals = (l.replace("\n", ("")).split(",") for l in single_line_gen)
#     capitals_dict = dict(countries_and_capitals)
#     print(capitals_dict)
    # print(next(countries_and_capitals))
    # print(next(countries_and_capitals))
    # print(next(countries_and_capitals))
    # print(next(countries_and_capitals))

def get_fibo():
    x=1
    y=0
    yield y
    while True:
        x, y = y, x
        x += y
        yield x
        # x += y
        # y = x
def inbo():
    for i in range(10):
        pass


fibo_gen = get_fibo()
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))


