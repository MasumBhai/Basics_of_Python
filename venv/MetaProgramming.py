info = """
In Python, functions are the first class objects, which means that:
-Functions are objects; they can be referenced to, passed to a variable and returned from other functions as well.
-Functions can be defined inside another function and can also be passed as argument to another function.

* Python has an interesting feature called decorators to add functionality to an existing code.
* This is also called metaprogramming because a part of the program tries to modify another part of the program at compile time.
* Decorators allow us to wrap another function in order to extend the behavior of wrapped function,without permanently modifying it.
* In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.
* Such functions that take other functions as arguments are also called higher order functions.
"""
print(info)

print("###nested function###")


def outer_function():
    print("outer function started")

    def inner_funtion():
        print("inner function started")

    print("inner funtion ended")
    print("outer function ended")


outer_function()  # inner function didn't invoked
print("\n###nested function with function arguments###\n")


def outer_function(function):
    print("outer function started")
    print("argument function started in outer function")
    function()
    print("argument function ended in outer function")

    def inner_funtion():
        print("inner function started")
        print("argument function started inside inner function")
        function()
        print("argument function ended inside inner function")

    print("This is before calling inner function")
    inner_funtion()
    print("inner funtion ended")
    print("outer function ended")


def arg_fun():
    print("argument function is working")


# outer_function(arg_fun())  # it will give error
outer_function(arg_fun)

print("\n###python closure###\n")


def outer_func():
    message = "Hello from Masum Bhai"

    def inner_func():
        print("inner func is invoked")
        print(message)

    # return inner_func() # inner function will invoke
    return inner_func  # this will give address of inner func() as object


my_variable = outer_func()
print(my_variable)  # it will print address
my_variable()  # it will invoke outer_func()
print("----------------------")
new_my_variable = my_variable()
# new_my_variable() # it will give error
new_my_variable  # now it will act as my_variable()
print("----------------------")


def outer_func(message):
    def inner_func():
        print("inner func is invoked")
        print(message)

    return inner_func


second_variable = outer_func("Masum The Hero from zero")
second_variable()

print("""\n###Decorator###\n""")


def old_deccorator(old_function):
    def inner_old_function():
        print("i'm inside inner_old_function")
        return old_function()

    return inner_old_function


def new_decorator(new_function):
    def wrapper_func():
        print("i'm inside wrapper function")
        return new_function()

    return wrapper_func


@old_deccorator
@new_decorator
def super_fun():
    print("Hail Hydra")


super_fun()

print("""\n###Word count programme using Decorator###""")


def split_string(name):
    def wrapper():
        split = name().split()
        return len(split)

    return wrapper


@split_string
def normal_string():
    str = input("Enter sentence or paragraph to count it's word (no enter key allowed):\n")
    return str


print("Total word count:", normal_string())
