#  use range to count down
for i in range(5, -1, -1):    # it count down from 5 to 0
    print(i, " ", end="")
for i in range(10, -1, -1):   # it count down from 10 to 0
    print(i, " ", end="")
# similar logic, count down from 100 to 1 is range(100,0,-1), understand its logic
for i in range(100, 0, 1):
    print(i, " ", end="")


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
message = "Eligible" if 18 <= age < 65 else "not eligible"
print(message)


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


# This is how real code was writen in ,with in the main()
# In this way , you can define function at the end of the main content
"""
main():
    yourfuction1()
    yourfuction2()

def yourfuction1():
    pass

def yourfuction2():
    pass

if __name__="__main__":main()
"""


# This is called list comprehension
my_numbers1 = [x*x for x in [1, 2, 3, 4]]
my_numbers2 = [x*2 for x in range(1, 11)]
print(my_numbers1)
print(my_numbers2)

# This is a way to write short function in one line
def function_hello(yourname): print("Hello! ", yourname)

