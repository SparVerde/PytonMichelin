# class -> keyword
# convention -> class name are Capitalize
class Cat:
## special function initiate: def + space + _+_+init+_+_+(+self,+object)+:
## self is the reference of current object
    def __init__(self, name, age):
        ## self.name -> the object has an attribute called name
        self.name = name # self the current object self = this
        self.age = age
## special function: every parameters
    def __str__(self):
        #return "returned string"
        return f'The cat {self.name} has {self.age} years'


## Creating objects
cat_object1 = Cat('Rino', 5.5)
print(cat_object1)
print(cat_object1.name,cat_object1.age) #.to call an object
print(type(cat_object1))

a_string = str(cat_object1) # this call __str__ on the object
print("convereted string;", a_string)

cat_object2 = Cat('Pierre',7.5)
print(cat_object2)
#print(cat_object2.name)
#print(cat_object2.age)
