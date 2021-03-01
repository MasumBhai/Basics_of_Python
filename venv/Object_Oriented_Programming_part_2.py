info = """###inheritence###
**unlike java,c++ . python supports multiple inhreritence 
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Inheritance is a powerful feature in object oriented programming.

1. It represents real-world relationships well.
2. It provides reuse ability of a code. We don’t have to write the same code again and again.
Also, it allows us to add more features to a class without modifying it.
3.It is transitive in nature, which means that if class B inherits from another class A,
 then all the subclasses of B would automatically inherit from class A.
 
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.

-Create a Parent Class or Base class
Any class can be a parent class, so the syntax is the same as creating any other class:

-Create a Child Class or Sub class
To create a class that inherits the functionality from another class, send the parent class as a parameter

#Note: Use the pass keyword when you do not want to add any other properties or methods to the class.

**Adding __init__
When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
The child's __init__() function overrides the inheritance of the parent's __init__() function.
"""
print(info)


class Employee:
    def __init__(self, name, university, salary):
        # print("inside Employee class")
        self.university = university;
        self.name = name;
        self.salary = salary;
        print("welcome:", self.name, "\nyour salary:", self.salary, "Million only")

    def welcome(self):
        print("welcome:", self.name, "\nyour salary:", self.salary)

    pass


class Manager(Employee):
    pass


class Developer(Employee):
    def __init__(self, name, university, salary, programming_language):
        # Employee.__init__(self,name,university,salary) # this is advantageous when multiple inheritence occured
        super().__init__(name, university, salary)  # when using super(),don't need to use self key word
        self.programming_language = programming_language;
        print("this is constructor of Developer class")

    pass


obj1 = Employee("Abdullah", "MIST", 1)
obj2 = Manager("Al Masum", "MIST", 1.5)
obj3 = Developer("Abdullah Al Masum", "MIST", 1.2, "python")
total_salary = obj1.salary + obj2.salary + obj3.salary;
print("So in this company,salary alloted for Masum Bhai per month:", total_salary, "Million $ only")

print("""\n###MultiLevel Inheritence###""")


class A:
    variable_of_A = None;

    def __init__(self):
        print("inside constructor of A")

    pass


class B(A):
    def __init__(self):
        print("inside constructor of B")

    pass


class C(B):
    def __init__(self):
        print("inside constructor of C")


print("the problem is: it will not invoke it's super classes constructor")
object = C();
object.variable_of_A = "Masum Bhai"
print(object.variable_of_A)


class A:
    variable_of_A = None;

    def __init__(self):
        print("inside constructor of A")

    pass


class B(A):
    def __init__(self):
        super(B, self).__init__()
        print("inside constructor of B")

    pass


class C(B):
    def __init__(self):
        super(C, self).__init__()
        print("inside constructor of C")


class D(C):
    def __init__(self):
        super(D, self).__init__()
        print("inside constructor of D")


print("##problem solved & object of D is called")
object1 = D();
object1.variable_of_A = "Masum Bhai"
print(object1.variable_of_A)

print("""\n###multiple Inheritence###""")


class Q:
    def __init__(self):
        # super(Q, self).__init__()
        print("inside of constructor of class Q")

    pass


class R:
    def __init__(self):
        # super(R, self).__init__()
        print("inside of constructor of class R")

    pass


class S(Q, R):
    def __init__(self):
        Q.__init__(self)
        R.__init__(self)
        print("inside of constructor of class S")

    pass


objectt = S();
