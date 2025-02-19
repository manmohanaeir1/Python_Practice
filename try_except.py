# to prevent the program from crashing when an exception occurs
# we can use the try-except block

try:
    a = int(input("Enter first number: "))
    print(a)
except:
    print("Invalid input")