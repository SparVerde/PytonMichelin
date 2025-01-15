

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age } years'
    
    ##Class inheritance
class Dog(Animal):
    def bark(self):
        print('uf uf'*self.age)

class HungarianDog(Dog):
    def bark(self):
        print('vau'*self.age)

class RomanianDog(Dog):
    def bark(self):
        print('ham'*self.age)

class PolishDog(Dog):
    def bark(self):
        print('cha'*self.age)

class SerbianDog(Dog):
    pass # creation new class to add something or remove something

animal_obj = Animal('Boy',3)
print(animal_obj)

dog_obj = Dog('Spike', 10)
print(dog_obj)
dog_obj.bark()
#animal_obj.bark() #doesn't work as no object on animal