
mydetails = input("Enter some story of yours")
print("You have entered is", mydetails)

# we will use now conditional statement to display the character one by one 
# We know that, we had earlier see that we can get the length of the string as len(stringname) 

str_length = len(mydetails) 
print('Lenght of the string is', str_length)

for x in range(str_length):
    print(x)


