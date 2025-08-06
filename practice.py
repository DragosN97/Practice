from sys import get_asyncgen_hooks


class Animal():

    def __init__(self, weight = 1):
        self.weight = weight

class Dog(Animal):

    def __init__ (self, name, affection, weight):
        super().__init__()
        self.name = name
        self.affection = affection
        self.weight = weight

        if self.affection < 1 or self.affection > 10:
            print("Invalid number, please insert a number between 1 and 10")


    def __str__(self):
        return f"{self.name}, {self.affection}, {self.weight}"

    def __repr__(self):
        return self.__str__()




class Cat(Animal):

    def __init__(self, name, affection, weight):
        super().__init__()
        self.name = name
        self.affection = affection
        self.weight = weight

        if self.affection < 1 or self.affection > 10:
            print("Invalid number, please insert a number between 1 and 10")

    def __str__(self):
        return f"{self.name}, {self.affection}, {self.weight}"

    def __repr__(self):
        return self.__str__()


def gather_animals():
    zip_animals = []
    for d, c in zip(dog, cat):
        zip_animals.append(d)
        zip_animals.append(c)
    return zip_animals


def sort_animals(animals):
    animals.sort(key = (lambda x: x.affection))
    return animals


def filter_by_weight(animals, weight_limit):
    fat_animals = []
    return [animal for animal in animals if animal.weight >= weight_limit]

dog = [Dog("Mark", 4, 8),Dog("Lime", 4, 3), Dog("June", 9, 2), Dog("Hades",1, 25), Dog("Fin", 6, 6)]
cat = [Cat("Mai", 3, 1), Cat("Luna", 1, 2), Cat("Yale", 3, 3), Cat("Jumbo", 8, 4), Cat("Xena", 5, 2)]


a1 = Animal()
d1 = Dog("Lucifer", 4, 9)
c1 = Cat("Mia", 4, 1)
print (gather_animals())
print (sort_animals(gather_animals()))
print(filter_by_weight(gather_animals(), 3))





