#open('test.txt', 'w') # Open file for writing
#pen('test.txt', 'r') # Open file for reading
#open('test.txt', 'a') # Open file for appending
#open('test.txt', 'r+') # Open file for reading and writing


Count_country  = open('test.txt', 'r')  # Open file for reading

#print(Count_country.read())  # Read the content of the file
print(Count_country.readlines()[3])   # Read the content of the file line by line
Count_country.close()  # Close the file
