x = 0b10
print(x)
print(bin(x))

x = 0x12c
print(x)
print(hex(x))

# a + bi
x = 1+2j
print(x)

# the usage of determining a variable is empty or not.
name = " "
if not name.strip():
    print("name variable is empty.")

# a clean way of writing some if expressions
age = 30
if 18 <= age < 65:
    print("Eligible")

else:
    print("Not Eligible")

# it can also be writen as the following:

messege = "Eligible" if 18 <= age < 65 else "not eligible"
print(messege)


for letter in "python":
    print(letter)

for item in ["a", "b", "c"]:
    print(item)


# vsc   ctrl + /   comment out large section of code

# vsc     ctrl shift p   command platte  (setting the visual studio code)

# vsc  Ctrl+Alt+N run code (code runner)
# vsc  code runner setting runinterminal true
###############################################################################
# the dumb way

names = ["John", "Mary"]
found = False
for name in names:
    if name.startswith("J"):
        print("Found")
        found = True
        break  # to same time
if not found:
    print("Not found")

# the clean way, becase else will only be executed when for loop is completed without immediate break , it is the same with while loops , else only get execute when there is no break

names = ["John", "Mary"]
for name in names:
    if name.startswith("J"):
        print("Found")
        break  # to same time
else:
    print("Not found")


# how to actually conotate a function:
def increment(number: int = 10, by: int = 20) -> tuple:
    return (number, number+by)


print(increment(number=3, by=1))

# how to use multiple input as parameter


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(1, 2, 3, 4, 5))

# how to use keywords argument in function


def save_user_info(**user_info):
    print(user_info["name"])


save_user_info(id=1, name="admin")

# python , in python there are two types of scopes, local variables with function scope and the global variable with file scope.In python there no block level scope.


# odd cases, python create a new local varaible in function if you call global variable with in a funtion with the same value as the globle variable. in order to actually call a global variable within a function, you need to declear it explicitly. difference bewtween the following two functions:
# using global variable within a function is bad practice.

message = "a"


def greeting():
    global message
    message = "b"


def greeting2():
    message = "b"


# visual studio code       F9  insert breakpoint    F5 run debuging   F10 steping over the current point to the next executable code in debuging

# vsc  F11 go into the currently called function.
