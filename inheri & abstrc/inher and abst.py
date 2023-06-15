##single inheritance

class Animal:
    def fun(self):
        print("Quack")

class Dog(Animal):
    def fun1(self):
        print("Bark")

my_dog = Dog()
my_dog.fun() 
my_dog.fun1()
print("----------------------------------------------------------------")


##Multiple inheritance
class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  
d = Derived()  
print(d.Summation(10,20))  
print(d.Multiplication(10,20))  
print(d.Divide(10,20))
print("------------------------------------------------------------")
##Hierarichy inheritance
class Animal:
    def breathe(self):
        print("Breathing...")

class Cat(Animal):
    def meow(self):
        print("Meowing...")

class Dog(Animal):
    def bark(self):
        print("Barking...")

my_cat = Cat()
my_cat.breathe()  
my_cat.meow()    
my_dog = Dog()
my_dog.breathe()  
my_dog.bark()   

print("------------------------------------------------------------")


##multilevel inheritance

class Vehicle:
    def start(self):
        print("Starting vehicle...")

class Car(Vehicle):
    def drive(self):
        print("Driving car...")

class SportsCar(Car):
    def race(self):
        print("Racing sports car...")

my_sports_car = SportsCar()
my_sports_car.start() 
my_sports_car.drive()  
my_sports_car.race()
print("----------------------------------------------------")

##super class

class myclass:
     def __init__(self,country,state):
          self.country=country
          self.state=state
     def fun(self):
          print(self.country,self.state)


class myclass2(myclass):
     def __init__(self,name,age):
          self.name=name
          self.age=age
          super().__init__("India","Tamilnau")
     def fun1(self):
          print(self.name,self.age)
my=myclass2("virat",34)
my.fun1()
my.fun()
print("----------------------------------------------------")


##self.objet

class myclass:
     def __init__(self,country,state):
          self.country=country
          self.state=state
     def fun(self):
          print(self.country,self.state)


class myclass2:
     def __init__(self,name,age):
          self.name=name
          self.age=age
          
          self.object=myclass("India","Andhra Pradesh")
          self.object.fun()
     def fun1(self):
          print(self.name,self.age)
my=myclass2("virat",34)
my.fun1()
print("-----------------------------------------------------")

##abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

circle = Circle(5)
print(circle.calculate_area())  # Output: 78.5

rectangle = Rectangle(4, 6)
print(rectangle.calculate_area())  # Output: 24





