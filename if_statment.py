# if perticular concern is true then only it will execute the block of code

a =3 
b= 3 
if a > b:
    print("a is greater than b")

elif a==b:
    print("a is equal to b")    
else:
    print("b is greater than a")


value = input("Enter the value: ")

if type(value) == int:
    print("This is integer")

elif type(value) == float:
    print("This is float")
elif type(value) == str:
    print("This is string")

elif type(value) == bool:
    print("This is boolean")            
else:
    print("This is not a valid data type")
