from fnmatch import translate
from math import *

print("Python has 3 data types...")
print("Text type: str")
print("Numeric types: int, float")
print("Boolean type: bool")

a_variable = "MASUM_Boss"
b_variable = 44
c_variable = 3.99
d_variable = False
"""This is comment Line"""
print("data type of a_variable ", type(a_variable))
print("data type of b_variable ", type(b_variable))
print("data type of c_variable ", type(c_variable))
print("data type of d_variable ", type(d_variable))
print("""
""")
"""String Function"""
# Concatanation by , and +
a_string = "MASUM Bhai is the boss"
b_string = ",,,,,rrttgg.....banana....rrr"
c_string = "This Book is for only {price} dollars!"
print(a_string.swapcase())
print(a_string.title())
print(b_string.strip(",rtg."))  # Remove the leading and trailing characters
print(a_string.replace("Bhai", "Boss"))
print("This is split", a_string.split())
print("This is partition", a_string.partition("is"))
print(a_string.center(50))
print("In a_string 'i' occurs:", a_string.count("i"), "times")
print(a_string.center(50))
print("this is upper method:", a_string.upper())
print("in a_string variable 'Bhai' word found at index:", a_string.find("Bhai"))
print("This is format method", c_string.format(price=69))
print("""
""")
"""Numeric Data"""
a_math = 19
b_math = 7
res = a_math/b_math
print("res = a_math / b_math is equal:", res)
res = a_math // b_math
print("res = a_math // b_math is equal:", res)
res = round(a_math/b_math)
print("res = round(a_math/b_math) is equal:", res)
res = round(a_math/b_math,3)
print("res = round(a_math/b_math,3) is equal:", res)
res = pow(res,3)
print("res = pow(res,3) is equal:", res)
print("ceil(res) is:",ceil(res),"and floor(res) is:",floor(res),"and round(res) is:",round(res))
res = a_math % b_math
print("res = a_math % b_math is equal:", res)

print("""""")
a_input = input("float please: ")
b_input = input("integer please: ")
res = a_input + b_input
print("res = a_input + b_input is:",res)
res = float(a_input) + float(b_input)
print("res = float(a_input) + float(b_input) is:",res)