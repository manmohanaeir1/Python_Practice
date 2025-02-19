# bunch of code which perform specific task 


def greething_function(name):
    
    print("Welcome!!" + name)

greething_function("Manmohan")    
    


def my_function(*student):
    
    print("Welcome!!" + student[2])

my_function("Manmohan","Ram", "Shyam")    
    


def your_function(name, age):
    
    print('welcome' +name+  'you are '+(age)+' years old')

    name = input("Enter your students anme: ")
    age = input("enter age") 

your_function("Manmohan",40)    
        