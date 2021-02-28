info = """**CLASS**
In technical terms we can say that class is a blue print for individual objects with exact behaviour.

**OBJECT**
object is one of instances of the class. which can perform the functionalities which are defined in the class.

**__init__ method**
"__init__" is a reserved method in python classes. It is called as a constructor in object oriented terminology.
This method is called when an object is created
from a class and it allows the class to initialize the attributes of the class.
It is run as soon as an object of a class is instantiated

**self***
self represents the instance of the class
The word 'self' is used to represent the instance of a class. By using the "self" keyword we access
the attributes and methods of the class in python.It binds the attributes with the given arguments.

**cls***
cls represents the instance of the class
The word 'cls' is used to represent the instance of a class. By using the "cls" keyword we access
the attributes and methods of the class in python.It binds the attributes with the given arguments.

**Class variables**
-Class variables shared among all instances of class. Class variables should be same for for each instance.
-Instance variables is unique for each instance

**TYPES OF METHODS**
-To define a class method in python, we use @classmethod decorator.
A class method can be called by class directly or by an instance

-no need to instantiate an instance to call the class method
-But a instance method can only be called by an instance.
An instance method’s first parameter is the instance who calls it.
-Regular functions belong to objects and instances. You can call regular methods with instances

*Static Method*
- It does not matter whether we call a static method by class or instance.

Why Use Static Method ?
Because static methods don’t contain parameters about a specific class or instances.
We can totally define it as an independent function out of a class and use it as other normal functions out of classes.
"""
print(info)

class Car:
    def __init__(self,model,engine,navigation):
        print("constructor created")
        self.engine = engine;
        self.navigation = navigation;
        self.model = model;

    def property(self):
        if(self.engine == 4):
            print(self.model,"car has more power bro,awesome!!")
        else:
            print(self.model,"car will be upgraded soon!!")

    @classmethod
    def welcome(cls):
        print('Hey bro,this is a class method,and you can call by class name')

    @staticmethod
    def congrats():
        print('Hey,welcome from static method')
   # pass


BMW = Car("F729",3,True)
# BMW.model = "F729"
# BMW.engine = "3hp"
# BMW.navigation = True

Fords = Car("B707",4,True)
# Fords.model = "B707"
# Fords.engine = "4hp"
# Fords.navigation = True

Fords.property()
BMW.property()      #this is calling using obj
Car.property(BMW) # this is calling using class
Car.welcome()
Car.congrats()
BMW.congrats()