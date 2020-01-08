#The builtin functions of python 3.7

# input() is used to get input from the user

words=input("What is your name?") # put the prompt messege in the parantheses
                                  # the input value is assigned to the varable "words"
number=int(input("give me a number:")) # input is always string type
                                       # use needed function to get the type you actually need

# print() is used to print the content on screen

print("The words are {},and the number is {}".format(words,number)) # one way of formating string
print(f"The words are {words},and the number is {number}")          # another way of formating string

number_a=11.11111
number_b=99.99999

# the first 1 an 0 tell it the order of varables, and the .2 and .4 means to the second or fourth decimal point
print("The biger one is {1:.2},and the smaller one is{0:.4}".format(number_a,number_b)) 

# len() tell you the length of a variable
len_list=[1,2,3,4,5,6,7]
len_string="hello,welcome!"
len_dic={"James Gunn":"Awsome","Deniel Chazzele":"Bold"}
print(len(len_list),len(len_string),len(len_dic))

# split() it split the string accoding to the argument you give, it return a list object
split_string= "It! is! a! beautiful! day!"
split_words=split_string.split(" ")
split_bang=split_string.split("!")
print(split_words,"\n",split_bang)

# list() it generate a list varable from any iterable object
list_dict={"jack":21,"jane":16}
list_tuple=(1,2,3,4)
list_string="hello"
print(list(list_dict))
print(list(list_tuple))
print(list(list_string))

# range() generate iterable range object with intergers for you

for i in range(10):     # it generate 10 interger star from 0, 
    print(i)
for i in range(1,20,3): # it genertart start from 1,with step of 3, up till 20
    print(i)
print(type(range(10)))  # range() generate a range object and not a list

# a trick to use range to count down
for i in range(5,-1,-1):    # it count down from 5 to 0
    print(i," ",end="")

for i in range(10,-1,-1):   # it count down from 10 to 0
    print(i," ",end="")     

# similar logic, count down from 100 to 1 is range(100,0,-1), understand its logic











"""
Full list of Built-in Functions
       
        abs()
        delattr()
        hash()
        memoryview()
        set()
        all()
        dict()
        help()
        min()   
        setattr()
        any()
        dir()
        hex()
        next()  
        slice()
        ascii()
        divmod()
        id()
        object()
        sorted()
        bin()   
        enumerate()
        input()
        oct()
        staticmethod()
        bool()
        eval()
        int()
        open()
        str()
        breakpoint()
        exec()
        isinstance()
        ord()   sum()
        bytearray()
        filter()
        issubclass()
        pow()
        super()
        bytes()
        float()
        iter()
        print()
        tuple()
        callable()
        format()           OK
        len()
        property()
        type()
        chr()
        frozenset()
        list()
        range()
        vars()
        classmethod()
        getattr()
        locals()
        repr()
        zip()
        compile()
        globals()
        map()
        reversed()
        __import__()
        complex()
        hasattr()
        max()
        round()
"""
