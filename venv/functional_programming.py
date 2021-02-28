from functools import *

print("""###Lambda Function###""")
print("Lambda function is an anonumous function")
print("**lambda function can take any number of arguments but can only have one expression")
print("lambda function is useful when we used them as anonymous function inside another function")

square1 = lambda x: x * x
a = square1(5)
print(a)

subtraction1 = lambda x, y: x - y
b = subtraction1(23, 6)
print(b)

print("using lambda inside function")


def test(x):
    return (lambda y: x + y)


c = test(7)(8)
print(c)

print("""\n###using filter function with lambda###""")
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
renew_list = list(filter(lambda x: x % 2 == 0, my_list))
print(renew_list)

print("""\n###using map function with lambda###""")
second_list = list(map(lambda x: x % 2 == 0, my_list))
print(second_list)
third_list = list(map(lambda x: x * 2, my_list))
print(third_list)

print("""\n###using reduce function with lambda###""")
summ = reduce(lambda x, y: x + y, my_list)
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#         (1+2=3) (3+4=7)  (5+6=11)  (7+8=15)  (9)
print(summ)