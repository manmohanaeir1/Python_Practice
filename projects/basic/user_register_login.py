username = input("Enter your username: ")
password = input("Enter your password: ")

print('Your account has been created successfully')
print("Login now")

user = input("Enter your username: ")
passw = input("Enter your password: ")


if user == username and passw == password:
    print("Login successful")
else:
    print("Invalid username or password")
    