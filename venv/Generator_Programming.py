info = """
There is a lot of work in building an iterator in Python. We have to implement a class with __iter__() and __next__() method,
keep track of internal states, and raise StopIteration when there are no values to be returned.
This is both lengthy and counterintuitive. Generator comes to the rescue in such situations.
* Python generators are a simple way of creating iterators. All the work we mentioned above are automatically handled by generators in Python.
* Simply speaking, a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).
  It is fairly simple to create a generator in Python. It is as easy as defining a normal function, but with a yield statement instead of a return statement.
* If a function contains at least one yield statement (it may contain other yield or return statements), it becomes a generator function.
  Both yield and return will return some value from a function.
* The difference is that while a return statement terminates a function entirely, yield statement pauses 
  the function saving all its states and later continues from there on successive calls.
###python iterator###
Iterator in python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets.
The iterator object is initialized using the __iter__ method. It uses the next() method for iteration.
An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
###Generator###
Generator-Object : Generator functions return a generator object.
Generator-Function : A generator-function is defined like a normal function, but whenever it needs to generate a value,
                    it does so with the yield keyword rather than return. If the body of a def contains yield,
                    the function automatically becomes a generator function.
"""
print(info)
my_stri = "MasumBhai prefer Anime(2D) Girl than real(3D) Girl"
print("""###One Way of iterating###""")
my_var = my_stri.__iter__()
print(next(my_var), end="")
print(next(my_var), end="")
print(next(my_var), end="")
print(next(my_var), end="")
print(next(my_var), end="")

print("""\n###Another Way of iterating###""")
new_var = iter(my_stri)
print(new_var.__next__(), end="")
print(new_var.__next__(), end="")
print(new_var.__next__(), end="")
print(new_var.__next__(), end="")
print(new_var.__next__(), end="")

print("""\n###How actually for loop works###""")
lis = [4, 8, 16, 32, 64, 15, 3, 9, 13, 95, 72, 34, 89, 64, 79, 40, 55, 98, 11, 18, 30, 82, 5, 984, 5883, 201, 531942]
my_list = iter(lis)
while True:
    try:
        print(my_list.__next__(), end=" ")
    except StopIteration as err:
        print(err)
        break
print("**using for loop:")
for x in lis:
    print(x, end=" ")

print("\n\n###Little bit of code###")


def square_num(num):
    sq_list = []
    for x in num:
        x = x * x
        sq_list.append(x)
    return sq_list


print(square_num(lis))
print("But i want to print a small portion of this square number of list,Here comes generator")


def square_num2(num):
    for x in num:
        yield x * x


gen = square_num2(lis)
print(gen.__next__(), end=" ")
print(gen.__next__(), end=" ")
print(gen.__next__(), end=" ")
print(gen.__next__(), end=" ")

# print("\nor print the full list using for loop")
# for x in gen:
#     print(x, end=" ")

print("\nor print the full list using stopiteration method")
while True:
    try:
        print(next(gen),end=" ")
    except StopIteration:
        break
