##print("jaga")
###Arthematic operators
a = 10
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a**b)

#Assignment operators
a=10
b=4
a+=b
print(a)

# Comparision operator
a=5
b=4
a==b
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)

#Logical operators
a=2
b=3
print(a and b)
print(a or b)
print(not a)

#Bitwise operator
a=10
b=5
print(a & b)
print(a | b)
print(a ^ b)
print(~b)
print(a<<1)
print(a>>1)

#Membership operator
a=[1,2,3]
print(1 in a)
print(4 in a)
print(5 not in a)

#Identity operator
a=10
b=10
print(a is b)
print(a is not b)

# Terenary operator
a=10
b=20
max_number= a if a>b else b
print(max_number)

##If condition
a = 33
b = 200
if b > a:
  print("b is greater than a")

## if else condition
number = -10
if number > 0:
    print("Positive")
else:
    print("Negative")

## if elif else condition
number = 10
if number > 10:
    print("Greater than 10")
elif number < 10:
    print("Less than 10")
else:
    print("Equal to 10")

## For loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
for x in "banana":
 print(x)

#break condition in for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


## continue statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#Range function in for loop
for x in range(6):
  print(x,end= ' ''\n',)
  
for y in range(2,6):
 print(y,end=' ',)
 
for z in range(2,30,3):
 print(z)

## else condiion in for loop
for x in range(6):
 print(x)
else:
  print("Finally finished!")

for x in range(6):
  if x == 3: break
  print(x)


##While loop
i = 1
while i < 6:
  print(i)
  i += 1

##i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


##Indexing
s=["apple","banana","cherry"]
print(s[0])

##slicing
s=["apple","banana","cherry"]
print(s[0:2])

##Int datatype
a=10
print(a)
print(type(a))
print(bin(a))
print(oct(a))
print(hex(a))

####float data type
a=10.23
print(type(a))
b=4.7e6
print(b)

##complex
a= 2+8j
print(a.real)
print(a.imag)

## strings
a="The sun rises in the east"
print(a)
                 
a='''The sun
     rises in the
     east'''
print(a)
              
a='The sun rises\n in the east'
print(a)

##Bytes

l=bytes([10,20,10,20,30,40])
print(l)
l=bytearray([10,20,10,20,30,40])
print(l)
l[0]=100
print(l)
print(l[0])

##List
l=[10,'sri',2+3j,{1,2,3},12.34]
print(l)
l[0]=34
print(l)
print(l[0])
l[1:2]
print(l)
l.append(10)
print(l)
l.insert(2,234)
print(l)
tropical = ["mango", "pineapple", "papaya"]
l.extend(tropical)
print(l)
l.remove(234)
print(l)

##SET
s={10,10,20,'sri',5-6j,34,34}
print(s)
print(type(s))                               
s.add(30)
print(s)
s.remove(30)
print(s)
                                 












