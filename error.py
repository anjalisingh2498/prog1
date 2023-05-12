list = [2,4,0,6,0,8]
for i in range(0, len(list)-1):
    try:
        print("Division:-", list[i]/list[i+1])
    except ZeroDivisionError:
        print("ZeroDivision Error")


try:
    from prg import*
    print("Successful")

except ModuleNotFoundError:
    print("ModuleNot FoundError")

try:
    even_numbers = [2,4,6,8]
    print(even_numbers[5])
except ZeroDivisionError:
    print("Denominator cannot be 0.")
except IndexError:
    print("Index Error")


try:
   result="Answer is " + 42
   print("Successful")
except TypeError:
   print("TypeError")

try:
    f=open("one.txt", 'r')
    print("Successful")

except FileNotFoundError:
    print("FileNot Found Error")
try:
    f=opens("one.txt", 'r')
    print("Successful")

except NameError:
    print("NameError")

try:
    f=open("one.txt", 'w+')
    f2=open("f2.txt", 'r')
    f2.write("newline")
    print("Successful")

except IOError:
    print("IOError")

try:
    f=open("one.txt", 'z')
    print("Successful")

except ValueError:
    print("Value Error")
