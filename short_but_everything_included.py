# from greatlearning
# python token : smallest meaningful component in programme
# python token : Keywords,operator,literals,identifiers
# identifiers : name used for python variables, functions or objects
# Literals : literals are nothing but constant

str1 = 'My name is Masum';
str2 = "My Name is Abdullah"
str3 = '''My Name is Al 
and i love to sit in between 
of masum and abdullah'''

print(str3);
print(str1[11]);
print("first charachter of 'Masum' is : " + str(str1.find("Masum")))
print(str1[15]);
print(len(str1))
print("In str3 number of 'a' is : " + str(str3.count('a')))
print(str1.replace('M', 'K', 1))
print(str1[11:16]);
print("Now i want to use split method in str3 ." + str(str3.split(' ')))
print(10 / 3)
# STRING jUSTIFY BASICALLY SPACE
print("Masum The Hero".rjust(30, '*'))
print("Masum The Hero".ljust(30, '*'))
print("Masum The Hero".center(30, '*'))
print("""""")
# Data structure in Python : 4 types,Tuple,list,dictionary,set
# Tuple : Tuples are here is almost like same as automata
# Tuples are immutable & ordered collection of elements enclosed with () brackets
tuple1 = ('a', "Masum", 2, 3 + 4j, True)
print(tuple1[1:4])
print(type(tuple1))
print("now i want to extract element from tuple. the last element is " + str(tuple1[-1]))
print("now i want to extract all element from tuple. " + str(tuple1[0: -1]))
print("here i didn't see the last element,where is it?")
print("Once again,now i want to extract all element from tuple. ")
x = tuple1.index(tuple1[-1])  # last element is index x
print(tuple1[0:x])
print("length of tuple : " + str(len(tuple1)))
print("""""")

# LIST are mutable enclosed with []
list1 = ['x', "Masum Bhai", 404, 420 + 5j, False]
print("list1's type : " + str(type(list1)))
print(list1[3])
u = len(list1)
print(list1[0:u])
list1.append("Boss")
list1[0] = 100
print(list1)
list1.insert(1, "Cool Boss")
print(list1)
list1.pop()
print(list1)
list1.reverse()
print(list1)
print("""""")

# Dictionary is also mutable using {} enclosed
dick1 = {"apple": 50, "Guava": 26, "Banana": 45, "Malta": 55, "Orange": 60, "Chocolate": 10}
print(type(dick1))
print(dick1.keys())
print(dick1.values())
dick1["apple"] = 100
print(dick1)
dick2 = {"cap": 60, "condom": 100, "T-shirt": 100, "Belt": 250, "Bra": 450, "Shoes": 500, "Underwear": 200,
         "spectacles": 750}
dick1.update(dick2)
print(dick1)  # here i just append 2 dictionary
dick2.pop("Bra")
print(dick2)

# if statements
if "apple" in dick1:
    print("correct")
else:
    print("incorrect")

# a = input("Input a number : ")
# print(type(a))  # input() always consider input as string
# print("Your number is : " + a)
# b = input("input different number : ")
# print("Your number is : " + b)

# Operator Precedence
print(
    "Operator Precedence : **,~,unary plus,unary minus,*,/,+,-,<<,>>,&,^,|,<,>,<=,>=,==.!=,=,+=,*=,-=,/=,is,is not,in,in not,&&,||")
xy = 4 + 4 / 10 * 4 - 1
print(xy)  # gives priority left most

stri = '''I study Computer Science in a public university named MIST,Bangladesh and during this 'corona session' my univerity is closed.I used to earn money by tutoring but this also has been stopped for about 8 months.All my friends are giving tours but i can't because of money.So,I'm stuck in my house,help my parents & sometimes do some programming.Now if i have the chance of getting financial help,i'll do my best to complete courses to grow my programming related skill as well utilize my time(actually certificate really matters as i'm in economic hardship).Oh! i forgot to mention that,I even don't have any debit or credit card.Therefore,please consider my situation. '''
print(len(stri.strip().split(" ")))  # word count in string
print("""""")
i = 1;
n = 4
while i <= 10:
    print(n, " * ", i, " = ", n * i)
    i += 1;
print("""""")
for val in dick1:
    print(val)

for x in dick1:
    for y in dick2:
        print(x, y)

print("""""")


# functions
def Hello():
    return "Hello, My boy!"


bc = Hello()
print(bc + "I am your Sir")
print("""""")

cube = lambda p: p * p * p  # LAmbda Function
print(cube(3))

# Lambda with Filter
li = [20, 65, 98, 15, 634, 687, 321, 48, 879, 21, 86, 48, 34, 420, 5468, 108, 565, 800]
final_List = list(filter(lambda x: (x % 2 != 0), li))  # Odd number filter korlam
print(final_List)
# lambda with map
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(lambda x: x * 2, lis)))  # 2 SE MULTIPLY KIYA
# lambda with reduce
from functools import reduce

print(reduce(lambda x, y: x + y, lis))  # this will give us sum of lis elements
print("""""")


# class
class Phone:
    def make_call(self):
        print("I can call")

    def play_game(self):
        print("I can play mobile games")

    def set_color(self, color):
        self.color = color

    def set_cost(self, cost):
        self.cost = cost

    def show_color(self):
        return self.color;

    def show_cost(self):
        return self.cost;


object_of_Phone = Phone()
object_of_Phone.set_cost(10000)
object_of_Phone.set_color("Black")
print(object_of_Phone.show_cost())
print(object_of_Phone.show_color())


# inheritation
class Vehicle:
    def __init__(self, milage, cost):
        self.milage = milage
        self.cost = cost

    def show_details(self):
        print("Vehicle's milage is :", self.milage)
        print("Vehicle's cost is :", self.cost)


car1 = Vehicle(120, 1050000)
car1.show_details()


class Truck(Vehicle):
    def car_Details(self):
        print("Hello! I am Mr. Truck")


class Truck(Vehicle):
    def __init__(self, milage, cost, tyres, horse_power):
        super().__init__(milage, cost)
        self.tyres = tyres
        self.horse_power = horse_power

    def show_Truck_details(self):
        print("I am a Truck a sub-class of Vehicle")
        print("Tyre numbers : ", self.tyres)
        print("Horse Power is : ", self.horse_power)


# car2 = Truck(80, 550000)
# car2.show_details()

car3 = Truck(100, 850000, 6, 720)
car3.show_details()
car3.show_Truck_details()
