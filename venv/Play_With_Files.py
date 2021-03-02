myfile = open("AlienFile.txt","r")
if myfile.readable():
    print("####################################################")
    print(myfile.read())
    print("####################################################")
    # print("####################################################")
    # for elements in myfile.readlines():
    #    print(elements)
    # print("####################################################")
myfile.close()