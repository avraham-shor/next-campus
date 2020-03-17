count_animals = 0
class Cow():

    def __init__(self,name="anonimus"):
        self.name = name
        self._age = 0
        global count_animals
        count_animals += 1


    # def birthday(self):
    #     self.age += 1
    #
    # def get_age(self):
    #     return self.age

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

class BigThing:
    def __init__(self, x):
        self.x = x

    def size(self):
        return self.x if str(self.x).isnumeric() else len(self.x)

class BigCat(BigThing):
    def __init__(self, x , wage):
        BigThing.__init__(self, x)
        self.wage = wage


    def size(self):
        if self.wage > 20:
            return "Very Fat"
        elif self.wage > 15:
            return "Fat"
        else:
            return "OK"













def main():
    shor1 = Cow("shor1")
    shor2 = Cow()
    print(shor1.get_name())
    print(shor2.get_name())
    shor2.set_name("Hoks")
    print(shor2.get_name())
    print(count_animals)
    # shor1.birthday()
    # shor1.birthday()
    # shor2.birthday()
    my_thing = BigThing("balloon")
    print(my_thing.size())
    cutie = BigCat("mitzy", 33)
    print(cutie.size())
main()
