##sample class and object
class MyClass:
  x = 5

  
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)


##class and object using init

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

##creating different objects:

class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p1 = Person('sri')
p2 = Person('Vijay')
p3 = Person('shameer')

p1.say_hi()
p2.say_hi()
p3.say_hi()


##OUTSIDE FUCNTION:
class Dog:
    attr1 = "mammal"
    attr2 = "dog"
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)

Rodger = Dog()
print(Rodger.attr1)
Rodger.fun()









            

