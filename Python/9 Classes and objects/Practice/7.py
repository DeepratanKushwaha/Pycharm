# create class pets from class animals and further create class dog from pets
# add method bark to class dog

class Animals:
    animalType = 'Mammel'


class Pets(Animals):
    color = 'White'


class Dog(Pets):
    @staticmethod
    def Bark():
        print("hue hue hue hue!!! ")


d = Dog()
d.Bark()
