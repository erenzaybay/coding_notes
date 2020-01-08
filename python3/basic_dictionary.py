target={}                                        # initializing a dictionary variable
target["eren"]="hangzhou"                        # adding elements one by one
target["adina"]="shanghai"
target2=dict(eren="hangzhou",adina="shanghai")   # using dic() to construct a dictionary , it is better to use this
target3={"eren":"hangzhou","adina":"shanghai"}   # making a dictionary directly
print(target,target2,target3)

element=target["eren"]                           # you can do it this way, but it is not ideal
element=target.get("eren","the name is not found") # it is better to use get method to access the date,
print(element)                                   # it return the value of the key "eren", 
                                                 # if "eren" is not found , return the default value

element=target.pop("adina")                      # it return the value of the key adina , and remove
print(element,"##",target)                       # adina key value pair at the same time
 


target["eren"]="kulja"                           # you can change the key pair in a dictionary

dict1=dict(a=1,b=2,c=3)                          # you can combine the two or more dictionaries
dict2=dict(d=4,e=5,f=6)                          # they can't have shared keys
dict3=dict(**dict1,**dict2)                      # use ** to indecate that it is a dictionary type
dict4=dict(x=5,z=8,**dict1)                      # you also can do this
print(dict3)
print(dict4)


print("a" in dict4)                              # check if a is in dict4
print("a" not in dict4)                          # check if a is not in dict4

keys_object = target.keys()                      # keys_object is dict_keys(["eren","adina"])
keys_list = list(keys_object)                    # keys_list is a list ["eren","adina"]
values_object = target.values()                  # value_object is dict_values(["kulja","shanghai"])
values_list =list(values_object)                 # values_list is a list ["kulja","shanghai"]
print(keys_object,keys_list,values_object,values_list)

answer= "eren" in target                         # checking the existence of key "eren",return boolean
answer2= "eren" not in target                    # checking the non-existence of key "eren",return boolean

print(answer,answer2)

del target["eren"]                               # delete the "eren":kulja key value pair
print(target)

target.clear()                                   # it clear the content of dictionary
print(target)

del target                                       # it delete the target variable compeletly
