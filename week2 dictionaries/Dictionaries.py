##dictionary example
d = {
  "brand": "vw",
  "model": "polo",
  "year": 1975
 
                }
print(d)
##
####Duplicates not allowed
d = {
  "brand": "vw",
  "model": "polo",
  "year": 1975,
  "year": 2000
                }
print(d)
##
####length of dictionary
print(len(d))
##
####Different data types:
d = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(d)
##
####Adding new key and value to the existing one
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) 
car["color"] = "white"
print(x)
x = car.values()
print(x)
if "model" in car:
 print("Yes, 'model' is one of the keys in the car dictionary")

##Acessing values and keys
d =	{
  "brand": "Hyundai",
  "model": "Verna",
  "year": 1975
}
for x in d.values():
   for x in d.keys():
      print(x)
##Accessing key and values at a time.
d ={
  "brand": "Mahindra",
  "model": "Thar",
  "year": 2023
}

for x, y in d.items():
  print(x, y)
##Attaching values to keys.
x = ('k1', 'k2', 'k3')
y = 1
d = dict.fromkeys(x, y)
print(d)


##Setdefault functions
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")
print(x)




