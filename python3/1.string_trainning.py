target1 = "Is your code name '007'"
target2 = 'a'
target = "have to add"
target[0]
target[1]

# first included, last one not included
target[3:8]
target[3:]
target[:3]
target[:]
print(target[-1])
print(r"good for path'c:/windows/secret/topsecret', or 'regular expression'")
print(f"Your line is {target},and {target}")

target3 = '''\
This is how you use long string,
 "\" in the first line will be ignored.
'''

print("Your line is {},and {}".format(target, target2))

string_1, string_2, string_3 = "one", "two", "three"
print("The second is {1}, the third one is {2}, and the first one is {0}".format(
    string_1, string_2, string_3))

# you can use a dictionary, and the same variable can be refereed many times
num_1 = 111
num_2 = 222
my_dictionary = dict(foo=num_1, bar=num_2)
print("The big number is {bar}, the small number is {foo}, the small number is {foo}".format(
    **my_dictionary))

"A MOVIE IS A GOOD ONE".upper()
"A Movie Is A Good One".capitalize()
"a movie is a good one".lower()
"a mOVIE iS a gOOD oNE".swapcase()

target3.find("return the index of the first occurrance")

target3.replace("to be replaced element,all occurrance", "the new element")

"ttt123ttt".strip("ttt")
"    the white space  ".strip()

"only remove white space at end of the line   ".rstrip()
"this string has a new line ending\n".rstrip("\n")
"only remove if it exist".rstrip("st")

"abcdefg123".isalnum()

list_object = "Default is splitting at white space".split()

list_object = "Or you can specify a rule".split("o")

joined_words_1 = " ".join(word_list_1)    # joined by " "
joined_words_2 = "@@".join(word_list_1)   # joined by "@@"
