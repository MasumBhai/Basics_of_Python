import traceback

print("###Exception Handling###")

list1 = ['A', 'E', 'I', 'O', 'U']
try:
    print(10 / 0)
    print(list1.index('I'))
except ValueError:
    print("Errror occured")
except ZeroDivisionError as err:
    print(err)
except ArithmeticError:
    print("Arithmatic Error occured")
except Exception:
    traceback.print_exc()
except Exception as err:
    print("Eroor:", err)
else:
    print("No Error  occured")
finally:
    print("This is final Block")
    print(list1.index('I'))
