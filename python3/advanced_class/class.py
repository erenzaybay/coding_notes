class dog:

    eyes=2
    legs=4
    intelligence="smart"

    def __init__(self,**kwargs):
        self.dog_attribute=kwargs

    def set_dog(self,key,value):
        self.dog_attribute[key]=value

    def get_dog(self,key):
        return self.dog_attribute.get(key,None)

    @property                                           # This turn the function into a accesser  
    def color(self):
        return self.dog_attribute.get("color",None)

    @property
    def name(self):
        return self.dog_attribute.get("name",None)
    
    @name.setter                                        # This turn the functon into a setter
    def name(self,name):
        self.dog_attribute["name"] = name               # notice ! the nature and meaning of "name", ask you big brother
                                                        # is different , there are four "name" writen , it is three kind of things
    @color.setter
    def color(self,color):
        self.dog_attribute["color"] = color

    @color.deleter                                      # This turn the function into a deleter
    def color(self):
        del self.dog_attribute["color"]


gooddog=dog()
baddog=dog()

gooddog.set_dog("name","Wangcai")
baddog.name="Harry"

gooddog.set_dog("color","white")
baddog.color="black"

print(gooddog.get_dog("name"))
print(baddog.name)

print(gooddog.get_dog("color"))
print(baddog.color)



print("the gooddog's name is ",gooddog.get_dog("name"),"and it's color is ",gooddog.get_dog("color"))

print("the baddog's name is ",baddog.name,"and it's color is ",baddog.color)
