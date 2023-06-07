##Argumented functions
def my_function(*kids):
 print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

##key and values
def children(child3, child2, child1):
  print("The youngest child is " + child3)

children(child1 = "manashvi", child2 = "john", child3 = "Linux")

##Arbitrary Keyword Arguments, **kwargs:
def kids(**kid):
    print("His last name is " + kid["lname"])
    kids(fname = "john", lname = "wick")

####default function
def my_country(country="India"):
  print("I love my " +country)
my_country()


##List type functions
def my_fruits(food):
  for x in food:
    print(x)
fruits = ["Custard apple", "kiwi", "orange"]
my_fruits(fruits)

##Return value
def function(m1,m2,m3):
     var=m1+m2+m3
     return var
R=function(1,2,3)
print(R)



