import copy

print("###List Comprehension###")
print("it offers shorter syntax based on the existing list")
price = [100,150,200,170,520,350]
new_price = [x for x in price]
print("we will get same result")   # https://masumbhai.github.io/personal_portfolio/   about my info,plz visit 😅
print(new_price)
new_price = [x-10 for x in price]
print("we will get 10 minus from every elements in list")
print(new_price)

print("""\n####String Formatting using Dictionary###\n""")
firstname = "Abdullah"
lastname = "Masum"
information1 = "my first name is {} and my last name is {}".format(firstname.upper(), lastname.upper())
print(information1)
information2 = f"my first name is {firstname.lower()} and my last name is {lastname.lower()}"
print(information2)
data1 = f"4 times 11 is: {4 * 11}"
print(data1)
for i in range(1, 11):
    info = f"value of i is: {i:02}"
    print(info)

print("""\n####LIST###\n""")
lang = ["java", "python", "php", "c++", "javascript", "c", "html-css"]
lang_2 = ["Dart", "kotlin", "C#", "Swift", "R"]
lang3 = copy.deepcopy(lang_2)
print("deepcopy helps the shallow copy's problem.that is no changes will reflect")
print("till now language i know:", lang, " total no. is", len(lang))
print("but the best & easy to learn is:", lang[0:2])
print("language i want to learn:", lang_2)
lang3.insert(len(lang_2), lang)
print(lang3)
print("this is list under list,multidimentional list")
lang.extend(lang_2)
print(lang)
print("Now this is in one list")
lang.sort()
print("sorted lang list:", lang)
print("index of python in lang:", lang.index("python"))
lang.sort(reverse=True)
print("reverse sortred list:", lang)
print("another way of sorting", end=": ")
sortedd_list = sorted(lang)
print(sortedd_list)
print("This is join method:", " <-> ".join(sortedd_list))
print(lang.count(" <-> "), "so the join method doesn't included in list")
lang4 = ["Bangla", "English", "Arabic", "Hindi", "japanese"]
print("Language i know little bit", lang4)
lang4.clear()
print(lang4, "lang4 is cleared\n")

print("""####Tuples####\n""")
print("tuples are immutable and work as read only memory")
co_ordinates = ([3, 2, 7], [5, 1, 9])
print(co_ordinates)
print("1st vector point:", co_ordinates[0])
tupl1 = (7, 13, 17, 19)
tupl2 = (8, 12, 16, 20)
tupl3 = tupl1 + tupl2
print(tupl3)
print(len(tupl3))
print(tupl3 * 2)
print()

print("""####Dictionary####\n""")
print("tuples are not ordrered and can not be sliced")
dick1 = {'a': 1, 'b': 2}
dick2 = dict(xyz=1, pqr=2)
print("using {} method", dick1)
print("using dict method", dick2)
dick3 = {
    "name": "Masum",
    "address": "Dhaka,Bangladesh",
    "university": "MIST",
    "College": "NDC"
}
print(dick3)
print("objects inside dictionary3 is:", len(dick3))
keyss = dick3.keys()
print(keyss)
values = dick3.values()
print(values)
pop_value = dick3.pop("College")
print(pop_value)
print(dick3)
del dick3['university']
print(dick3)
dick3.clear()
print(dick3)

print("""\n####sets####\n""")
print("set is not ordered and can not be indexed and also can not be sliced")
set1 = {"Abdullah", "Al", "Masum"}
print(type(set1), set1)
A = {5, 25, 1, 45, 35}
B = {11, 25, 5, 8}
print(A, B)
print("length of set A:", len(A), "& length of set B:", len(B))
print("This is union operation", A | B)
print("This is intersection operation", A & B)
print("This is difference operation (A-B)", A - B)
print("This is subset operation (A<=B)", A <= B)
print("This is superset operation (A<=B)", A >= B)
print("why false,cause every B element is not included in A set\n")

def show(*lis,**dictionry):
    print("list items are : ",lis)
    print("dictionary items are : ",dictionry)
dick4 = {"dhaka":55,"Mawa":35,"Gajipur":70}
li1 = ["Gulistaan","Ramana","Farmgate","Karwan-Bazar"]
show(li1,dick4)
print("just observe the diiferences")
show(*li1,**dick4)

print()
def printer(name):
    return name;

n = printer("Masum gets")
print(n)
n = printer("4.00")
print(n)
n = printer(False)
print(n)

