## for loop in set
set = {"apple", "banana", "cherry"}
for x in set:
    print(x)

##check the object if it is present in set
s={"apple","banana","orange"}
print("orange" in s)

##adding the element
s={"banana","kiwi","watermelon"}
s.add("custurd apple")
print(s)

##update the set with other set
s = {"apple", "banana", "cherry"}
ss = {"pineapple", "mango", "papaya"}
s.update(ss)
print(s)

##update the set with list
s = {"apple", "banana", "cherry"}
l = ["kiwi", "orange"]
s.update(l)
print(s)

##remove or discard the element in set
s={"apple","banana","custard apple","doggy","elephant"}
s.remove("doggy")
s.discard("elephant")
print(s)


##pop the element in set. it will done randomly
s={"apple","banana","custard apple","doggy","elephant"}
s.pop()
print(s)


s={"apple","orange","jungle"}
for x in s:
 print(x)

##union of two sets
s1 = {"a", "b" , "c"}
s2 = {1, 2, 3}
s3 = s1.union(s2)
print(s3)



set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

##intersection of two sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)


##symetric of two sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
