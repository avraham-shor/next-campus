


class Animal:
    """A sub class that testator for all animal class """
    def __init__(self, _name, _hunger=0):
        self._name = _name
        self._hunger = _hunger
        self.ZOO_NAME = "Hayaton"

    def get_name(self):
        ":returns the name of the animal"
        return self._name

    def is_hungry(self):
        """:returns True if the animal is hungry ,
        :returns False if the animal isn't hungry"""
        return self._hunger > 0

    def feed(self):
        "add 1 point to the measure-hungry of the animal"
        self._hunger -= 1

    def talk(self):
        "Prints the syllable of the specific animal"
        print("all animals")

    def __str__(self):
        print(self.__class__.__name__, self._name)


class Dog(Animal):

    def talk(self):
        """Prints the syllable of the specific animal,
         Overrides the function from the sub class"""
        print("woof woof")

    def fetch_stick(self):
        """a special method of Dog-class
        printed 'There you go, sir!'"""
        print("There you go, sir!")


class Cat(Animal):

    def talk(self):
        """Prints the syllable of the specific animal,
         Overrides the function from the sub class"""
        print("meow")

    def chase_laser(self):
        """a special method of Cat-class
                printed 'Meeeeow'"""
        print("Meeeeow")


class Skunk(Animal):
    def __init__(self, _name, _hunger=6):
        Animal.__init__(self, _name, _hunger)

    def talk(self):
        """Prints the syllable of the specific animal,
                 Overrides the function from the sub class"""
        print("tsssss")

    def stink(self):
        """a special method of Skunk-class
                printed 'Dear lord!'"""
        print("Dear lord!")


class Unicorn(Animal):

    def talk(self):
        """Prints the syllable of the specific animal,
           Overrides the function from the sub class"""
        print("Good day, darling")

    def sing(self):
        """a special method of Unicorn-class
                printed 'I’m not your toy...'"""
        print("I’m not your toy...")


class Dragon(Animal):
    def __init__(self, _name, _hunger=0, _color="Green"):
        Animal.__init__(self, _name, _hunger)
        self._color = _color
    def talk(self):
        """Prints the syllable of the specific animal,
         Overrides the function from the sub class"""
        print("Raaaawr")

    def breath_fire(self):
        """a special method of Dragon-class
                printed '$@#$#@$'"""
        print("$@#$#@$")



def special_mechod(instanch):
    """checks optometry the special method of this animal"""
    if isinstance(instanch,Dog):
        instanch.fetch_stick()
    elif isinstance(instanch, Cat):
        instanch.chase_laser()
    elif isinstance(instanch,Skunk):
        instanch.stink()
    elif isinstance(instanch,Unicorn):
        instanch.sing()
    elif isinstance(instanch,Dragon):
        instanch.breath_fire()


def main():
    "The main method call for all methods"
    dog = Dog("Brownie",10)
    cat = Cat("Zelda",3)
    skunk = Skunk("Stinky")
    unicorn = Unicorn("Keith",7)
    dragon = Dragon("Lizzy",1450)
    doggo = Dog("Doggo", 80)
    kitty = Cat("Kitty", 80)
    dStinky = Skunk("Stinky Jr.", 80)
    clair = Unicorn("Clair", 80)
    mcFly = Dragon("McFly", 80)
    zoo_lst = [dog, cat, skunk, unicorn, dragon, doggo, kitty, dStinky, clair, mcFly]

    for animal in zoo_lst:
        animal.__str__()
        animal.talk()
        special_mechod(animal)
        while animal.is_hungry():
            animal.feed()
    print(dog.ZOO_NAME)
if __name__ == '__main__':
    main()


