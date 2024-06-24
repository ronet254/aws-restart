mystring="This is a string"
print(mystring)
print(type(mystring))
print(mystring + " is of data type " + str(type(mystring)))
firstsring = "water"
secondstring = "fall"
thirdstring = firstsring + secondstring
print(thirdstring)
name = input("what is your name")
wife = input("what is the name of your first wife?")
wife2 = input("what is the name of your second  wife?")
children = input(" How many children do you have  from the first wife?")
children2 =  input(" How many children do you have  from the second  wife?")
names1 = input(" What are the names of your children from the first wife?")
names2 = input(" What are the names of your children from the second wife?")
print ("{}, your first wife is  called  {},  your second wife is  called  {},  you have {}  children from the first wife and {} from your second wife. the names of your children from your first wife are {} and names of your children from your second wife are {} ".format(name,wife,wife2,children,children2,names1,names2 ))