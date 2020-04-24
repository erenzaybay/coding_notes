target='I is just "great"!'
target2="Is your code name '007'"
target3="aAbBcCdD"
print(target[0],target[1],target[ 10],end=" ") # result: I   "  You can use index to call the individual elements
print(target[3:8])                             # frist included, last one not included
print(target[3:])                              # index 3 to the last string element,included
print(target[:3])                              # from the begining to the third string element ,not included
print(target[:])                               # choose them all
print(target[-1])                              # negetive number read from the end of the string
print(r"c:/windows/secret/topsecret")          # r means raw data ,it is useful for regex or path
print(f"Your line is {target},and {target2}")  # f means format


# This is how you use long string, "\" in the first line will be ingnored.
target3='''\
It is a lovely day,
we all like to walk in the sun,
and eat some fish.
'''
print(target3)



# The usage of format
print("Your line is {},and {}".format(target,target2)) # another way of formating

string_1="one"
string_2="two"
string_3="three"
print("The second is {1}, the third one is {2}, and the first one is {0}".format(string_1,string_2,string_3)) # you can specify the order and location

# you can use a dictionary, and the same variable can be refered many times
num_1=111
num_2=222
my_dictionary=dict(foo=num_1,bar=num_2)
print("The big number is {bar}, the small number is {foo}, the small number is {foo}".format(**my_dictionary))

# some basic string methods
print(target3.upper())                          # You get the uppercase string
print(target3.capitalize())                     # You uppercase the first letter of the string
print(target3.lower())                          # You lowercase all the string
print(target3.swapcase())                       # You swap the cases ,upper to lower and lower to upper 


print(target3.find("cC"))                       # return the index of the string's begning

print(target3.replace("cC","hahaha"))               # find all the "cC" and replace them with "hahaha"

print("ttt12234ttt".strip("ttt"))               # strip away the string from begning and the end
print("ttt1234ddd".strip("ttt"))
print("aaa1234ttt".strip("ttt"))                 # strip away them if they are there, but not if they are not there
print("    this line have white space    ".strip())             # By default ,it strip the white space

print("    only remove end of the line while spaces    ".rstrip())   # only remove the white space at the end of the line
print("this string has a new line ending\n".rstrip("\n"))            # how you specify the removal part

print("abcdefg123".isalnum())  # this test if all the content only alpha letter and numbers
print(" abcdefg123".isalnum()) # the result is false, becasue this is a " " in it

print("abc".isalpha())   # the result is true, because they are all alpha letters
print("111".isdigit())   # the result is true, because they are all digits
print("111.111".isdigit()) #the result is false ,because there is a "." in it


# spliting the string

long_string_1="This is an intertesting game,is it safe?"                 
long_string_2="                  This                 is an intertesting         game,is it safe?"
word_list_1=long_string_1.split()       # split() on default ,split at the whitle spaces
word_list_2=long_string_2.split()       # it could be many white spaces
print(word_list_1)                      # the result is a list object
print(word_list_2)
word_list_3=long_string_1.split("i")    # or you can specify the split point, "i" will be removed
print(word_list_3)

# joining the string
joined_words_1=" ".join(word_list_1)    # joined by " "
joined_words_2="@@".join(word_list_1)   # joined by "@@"
print(joined_words_1)
print(joined_words_2)
