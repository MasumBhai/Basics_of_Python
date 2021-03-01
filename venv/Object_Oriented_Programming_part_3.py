info = """
###Polymarphism###
different way of invoking polymarphism in python
1.different function
2.class method
3.objects to define polymarphism
###Abstruction###
An abstract class can be considered as a blueprint for other classes.
A class which contains one or more abstract methods is called an abstract class
It is a good practice of DRY (Don’t Repeat Yourself) principle
It allows you to create a set of methods that must be created within any child classes built from the abstract class.

While we are designing large functional units we use an abstract class
By default, Python does not provide abstract classes.
Python comes with a module which provides the base for defining Abstract Base classes(ABC) and that module name is ABC.
ABC works by decorating methods of the base class as abstract and registering concrete classes
as implementations of the abstract base.

A method becomes abstract when decorated with the keyword @abstractmethod.
from abc import ABC, abstractmethod

An abstract class has some features, as follows:

-An abstract method is a method that just has a declaration but does not have a detail implementation.
-An abstract class cannot be instantiated. It just provides an interface for subclasses to avoid code duplication.
-It makes no sense to instantiate an abstract class.
"""
print(info)


class Animal_Girl:
    def sound(self):
        print("Love u Masum Bhai!")


class CatGirl(Animal_Girl):
    def sound(self):
        print("Meaw meaw Masum Bhai!!!")


class BunnyGirl(Animal_Girl):
    def sound(self):
        print("Phew phew Masum Bhai!!")


def favourite_sound(girl_type):
    girl_type.sound();


Yume_chan = BunnyGirl()
Midori_chan = CatGirl()
Miyo_Sasaki = Animal_Girl()

favourite_sound(Miyo_Sasaki)
favourite_sound(Yume_chan)
favourite_sound(Midori_chan)

print("""\n###Help Function""")


class Fantasy_Girl:
    def __init__(self, type, name, sound):
        self.name = name
        self.type = type
        self.sound = sound

    pass


class AnimalGirl(Fantasy_Girl):
    list = ["Arachne", "centaur", "catgirl", "bunnygirl", "mermaid", "cowgirl", "dullahan", "puppygirl", "foxgirl",
            "wolfgirl", "birdgirl"]


class Cuteness(AnimalGirl):
    kawaii = "fluffy and kawaii"


fantasy1 = Fantasy_Girl("BirdGirl", "filo", "MasumBhai chuu")
help(fantasy1)
fantasy2 = Cuteness("WolfGirl", "Raphtalia", "MasumBhai,MasumBhai wolf wolf!!")
help(fantasy2)
print("### isinstance() ###")
print(isinstance(fantasy2, Animal_Girl))
print("\n### issubclass() ###")
print(issubclass(Cuteness, AnimalGirl))

print("""\n###magic method or special method or Dunder method###""")
print("it's nothing but having double underscore")


class Lolicon(Cuteness):
    def __len__(self):
        return len("Lolicon MasumBhai loves {} {}!!".format(self.kawaii,self.list[3]))
    def __str__(self):
        return ("Lolicon MasumBhai feeling shy to talk about {} {} named {},saying {}!!"
                "\nif __str__(self) is not used and print(object) is invoked then it eill return an address".format(self.kawaii,self.type,self.name,self.sound))


loli_no1 = Lolicon("foxgirl","Neko Para","Watashi o tabete hoshī,MasumBhai")
print(loli_no1)
print(len(loli_no1))
