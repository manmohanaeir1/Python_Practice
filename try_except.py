# to prevent the program from crashing when an exception occurs
# we can use the try-except block

try:
    a = int(input("Enter first number: "))
    print(a)
#except:

except ValueError:
    print("Invalid input")
    
finally:
    print("This is finally block")    