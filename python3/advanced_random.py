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
my_numbers1=[ x*x for x in [1,2,3,4]]
my_numbers2=[ x*2 for x in range(1,11)]
print(my_numbers1)
print(my_numbers2)

# This is a way to write short function in one line
def function_hello(yourname):print("Hello! ",yourname)


