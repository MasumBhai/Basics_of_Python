numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(numbers)
print(type(numbers))
for i in numbers:
    if i % 2 == 0:
        if i < 8:
            pass
            print(i)
            continue
        if i == 16:
            print("Oooh,I have reached my limit.Now's the time for break")
            break
        print(i)

# range function
for x in range(5):
    print(x, end=' ')

print("\nnow this will print (range's first element) to (range's last element -1)")
for c in range(1, 5):
    print(c, end=' ')

print("\nnow range with iteration ")
for x in range(1, 25, 2):
    print(x, end=' ')

print("\nagain range funtion with list,dictionaru,set,tuples")
for x in range(len(numbers)):
    print("at index", x, "element is", numbers[x])

# nested for loop
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
for i in range(3):
    for j in alphabets:
        print(j, end='_bug ')
    print()

print("\nlet's do pattern...")
for i in range(10, -1, -1):
    for j in range(i):
        print(j, end=' ')
    print()

#while loop
n=0
while n<5:
    print("alert!alert! Masum BHAI is sleeping now")
    n = n+1



