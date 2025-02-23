num1 = int (input("Enter first number: "))
num2 = int (input("Enter second number: "))
op = input("Enter operator: ")


if op == '+':
    print(int(num1) + int(num2))
elif op == '-':
    print(int(num1) - int(num2))
elif op == '*':
    print(int(num1) * int(num2))
elif op == '/':
    print(int(num1) / int(num2))  
else:
    print("Invalid operator")                    