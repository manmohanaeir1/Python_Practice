# used to get resonce from the task being performed by the function

def my_fun():
    return 4+5

print(my_fun())



def sum(num1, num2):
    return num1 + num2


num1 = int(input("Enter Number first: "))

num2 = int(input("Enter number second: "))
total = sum(num1, num2) 

print(total)