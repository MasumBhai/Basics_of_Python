from abc import ABC, abstractmethod

print("""\n###Abstruction###""")


class Computer:
    def __init__(self):
        print("i am groot..")

    @abstractmethod
    def powerMenu(self):
        print("first  need to power on computer")

    @abstractmethod
    def LockMenu(self):
        print("After opening Computer,need to put password in lock menu to open")

    def run(self):
        print("Computer programme is running")


class ShutDown(Computer):
    def powerMenu(self):
        print("After completely ShutDown disconnet power supply of computer")

    def LockMenu(self):
        print("press win+L key to go lock screen mode")


ob1 = ShutDown();
ob1.run()  # this is regular method
ob1.LockMenu()  # This is abstruct method
ob1.powerMenu()  # This is abstruct method

print("\n###Encapsulation###")


class Capsule:
    capsulation_package = "ediable"  # public variable
    __element = "chemical substances"  # private variable

    def time_to_eat(self):
        print("after eating,according to doctor's prescription")

    def __dosePerPerson(self):
        print("Doctor Masumhai will let you know soon.")


tablet = Capsule()
# print(tablet.__element)   #it will give error
# tablet.__dosePerPerson()  #it will give error
print(tablet.capsulation_package)
tablet.time_to_eat()
