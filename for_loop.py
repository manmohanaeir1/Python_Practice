# for loop is use for iteraiting over a sequence (list, tuple, dictionary, set, string)
for letters in 'Hello':
    print(letters)

    

print("\n")
myList = ['apple', 'banana', 'cherry']
for i in myList:
    print(i)

print("\n")

mydct = {'name':'Manmohan',
            'roll':23,
            'Address':'MNR',
            'firends':["Ram", "Shyam", "Hari"]
            }

for i in mydct:
    print(i)
    if i == "firends":
        break

print("\n")


mylist1 =   ['apple', 'banana', 'cherry']
for x  in range(3,7):
    print(x)
else:
    print("Finally finished!")    

          