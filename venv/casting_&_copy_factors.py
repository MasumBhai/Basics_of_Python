import copy

print("""###Casting###""")
print("casting could lead to data loss (float->int)")
print("casting is not applicable between any two types of data (int->list)\n")
info = """
Converts to a boolean
bool(obj) --> Boolean Converts to a list list(obj) --> list
Converts to a set
set(obj) --> set Converts to a tuple tuple(obj) --> tuple
Converts to an integer
int(obj) --> int Converts to a float float(obj) --> float
Converts to a string
str(obj) --> str Converts to a dictionary dict(obj) --> dict"""
print(info)

a = 1
print(type(a))
b = float(a)
print(type(b))
c = str(a)
print(type(c))

print("""\n###Shallow Copy###""")
car_dict1 = {"brand": "Ford", "model": "Mustang", "year": 1964}
car_dict2 = car_dict1
print("before changing")
print(car_dict1)
print(car_dict2)
print("after changing")
car_dict1["year"] = 1970
car_dict1["brand"] = "Mitshubishi"
print(car_dict1)
print(car_dict2)

print("""\n###Deep Copy###""")
car_dict3 = {"brand": "Ford", "model": "Mustang", "year": 1964}
car_dict4 = copy.deepcopy(car_dict3)
print("before changing")
print(car_dict3)
print(car_dict4)
print("after changing")
car_dict3["year"] = 1970
car_dict3["brand"] = "Mitshubishi"
print(car_dict3)
print(car_dict4)
