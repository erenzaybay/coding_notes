class dog:

    eyes=2
    legs=4
    intelligence="smart"

    def __init__(self,**kwargs):                  # it initialize it with a key word argument
        self.dog_attribute=kwargs

    def set_dog(self,key,value):
        self.dog_attribute[key]=value

    def get_dog(self,key):
        return self.dog_attribute.get(key,None)


gooddog=dog()

gooddog.set_dog("name","Wangcai")
print("the gooddog's name is ",gooddog.get_dog("name"),"and it's color is ",gooddog.get_dog("color"))

