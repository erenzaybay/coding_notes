# function with tuple as the argumet
# the tuple can not be changed,it is imutables
def function_with_tuple_simple(*args):
    for name in args:
        print(f"{name} is winner!")

function_with_tuple_simple("Jane","Jack","Jude","Jasimin")

winer_list=["Jane","Jack","Jude","Jasimin"]

# You can not directly use a list, it will see the list as an one element
function_with_tuple_simple(winer_list)   #check the result

# You need to use * to note that you want it to be splited
function_with_tuple_simple(*winer_list)  #check and compare the result    


# function with key word argumets as the argumet
# It is like a dictionary
# it is convention to name it **kwargs
def function_with_key_word_argument_simple(**kwargs):
    for key in kwargs:
        print(key,kwargs[key])

function_with_key_word_argument_simple(name="Eren",Age="33",gender="male")

#the named argument should at the begining
def function_with_tuple(complement,*names):
    for name in names:
        print(f"{name} is {complement}!")

function_with_tuple("the winner","Jane","Jack","Jude","Jasimin")

#the named argument should be at the begining
def function_with_key_word_argument(message,**kwargs): 
    print(message)
    for key in kwargs:
        print(key,kwargs[key])

function_with_key_word_argument("We have a soldier!",name="Eren",Age="33",gender="male")



# This example includes all the type we learned
# the order is important , the name argumet, the tuple argument and the key word arguments
def function_with_all(mynumber,mystring,*args,**kwargs):
    print(mynumber,mystring,args,kwargs["name"],kwargs["age"])       # you don't need to know what kwargs they may use ,see line 35

mylist=[132,32,32,4,5]
function_with_all(123,"hello",*mylist,name="Jack",age=15)   #compare the difference
function_with_all(123,"hello",mylist,name="Jack",age=15)
