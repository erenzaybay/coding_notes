
# use dir(__builtins__) to get the name of all the built in functions ,constants, and exceptions.
dir(__builtins__)


# use dir to get all the attributes and methods to any built in functions.
dir(abs)

input()
# input() is used to get input from the user
words = input("What is your name?")
number = int(input("give me a number:"))

print()
# print() is used to print the content on screen
print("The words are {},and the number is {}".format(words, number))
print(f"The words are {words},and the number is {number}")
number_a = 11.11111
number_b = 99.99999
# the first 1 an 0 tell it the order of varables, and the .2 and .4 means to the second or fourth decimal point
print("The bigger one is {1:.2},and the smaller one is{0:.4}".format(
    number_a, number_b))

len()
# len() tell you the length of a variable
len(len_list)   # number of items
len(len_string)  # number of character space
len(len_dic)    # number of key value pair

split()
# split() it split the string according to the argument you give, it return a list object
split_string = "It! is! a! beautiful! day!"
split_words = split_string.split(" ")
split_bang = split_string.split("!")
print(split_words, "\n", split_bang)


list()
# list() it generate a list varable from any iterable object
list_dict = {"jack": 21, "jane": 16}
list_tuple = (1, 2, 3, 4)
list_string = "hello"
print(list(list_dict))   # keys
print(list(list_tuple))
print(list(list_string))

range()
# range() generate iterable range object with intergers for you
range(5):         # 0,1,2,3,4
range(1, 10, 3):  # 1,4,7                      1 to 9 with the step of 3
print(range(10))  # range() generate a range object and not a list


bin()
# turn the value into binary number
x = 0b10
print(x)
print(bin(x))

# turn the value into hexadecimal number
x = 0x12c
print(x)
print(hex(x))
