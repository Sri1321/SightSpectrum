amount = 10000
if(amount > 2999)
print("You are eligible to purchase Dsa Self Paced")
print("------------------------------------------------------")
amount = 10000
if(amount > 2999):
print("You are eligible to purchase Dsa Self Paced")


x=23
s=x/0
print(s)

x = 5
y = "hello"
z = x + y
print(z)

x = 5
y = "hello"
try:
	z = x + y
except TypeError:
	print("Error: cannot add an int and a str")


a = [1, 2, 3]
try:
	print ("Second element = %d" %(a[1]))

	# Throws error since there are only 3 elements in array
	print ("Fourth element = %d" %(a[3]))

except:
	print ("An error occurred")

def fun(a):
    if a < 4:
        # throws ZeroDivisionError for a = 3
        b = a / (a - 3)

    # throws NameError if a >= 4
    print("Value of b = ", b)


try:
    # fun(3)
    fun(5)
#
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")

def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print (c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)



