myfruitslist = ["apple", "banana", "cherry"]
print(myfruitslist)
print(type(myfruitslist))
print(myfruitslist[0])
print(myfruitslist[1])
print(myfruitslist[2])
myfruitslist[2]="orange"
print(myfruitslist)
mytuple=("apple", "banana", "pineapple")
print(mytuple)
print(type(mytuple))
print(mytuple[0])
print(mytuple[1])
print(mytuple[2])
myfavouritefruitdictionary= { 
    "Akua" : "apple", "saanvi" : "banana", "Paulo"  : "pineapple"
    }
print(myfavouritefruitdictionary)
print(type(myfavouritefruitdictionary))
print(myfavouritefruitdictionary["Akua"])
print(myfavouritefruitdictionary["saanvi"])
print(myfavouritefruitdictionary["Paulo"])
mymixedtypelist=[45, 290578, 1.02, True, "my dog is in the bed.", "45"]
for item in mymixedtypelist:
    print(" {} is of the data type {}" .format(item,type(item)))