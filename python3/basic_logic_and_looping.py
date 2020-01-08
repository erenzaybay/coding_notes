# if ,elif,and else contruct a logic branch
foo=int(input("give me a number:"))
if foo>0:
    print("foo is larger than 0")
elif foo==0:
    print("foo is zero!")
else:
    print("foo is smaller than 0.")
    
# for loop through iterable objects
# looping through a list
for_list=[1,2,3,4,5]
for i in for_list:
    print(i)

# looping through a range interable
for i in range(10):
    print(i)

for i in range(5,8):
    print(i)

# while loop keep looping until the condition is met
while_answer=1
while while_answer<10:
    print(while_answer," ",end="")
    while_answer+=1
# looping technique:

# Using break ,break can be use in while loop or for loop to break outof the loop
while_number=1
while True:
    print(while_number," ",end="")
    while_number+=1 
    if while_number==10:
        break

for i in range(100):
    print(i," ",end="")
    if i ==10:
        break

print("#"*20)                 # remenber to remove the line

# You can iterate through a list , tuple, dictionary or range() object with enumerate(),which give you an index

trick_list=["eren","adina","zay","bay","harelhax"]
for index,element in enumerate(trick_list):
    print(index,element)

trick_tuple=("usa","china","japan","germany")
for index,element in enumerate(trick_tuple):
    print(index,element)

trick_dict={"eren":"movie","adina":"running","zay":"tea party","bay":"sleeping","harelhax":"eating"}
for index,key in enumerate(trick_dict):
    print(index,key)                             # it only print index and the keys ,not the values

for index,element in enumerate(range(8)):
    print(index,element)

# you can loop through a dictionary 

# first way of looping through a dictionary ,vey bad idea,don't do this
for key in trick_dict:
    print(key)

for key in trick_dict:
    print(key,trick_dict[key])

# the second way ,the prefered way is this
for key,value in trick_dict.items():
    print(key,value)
