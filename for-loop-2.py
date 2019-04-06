
mydetails = input("Enter some story of yours")
print("You have entered is", mydetails)

# we will use now conditional statement to display the character one by one 
# We know that, we had earlier see that we can get the lenght of the string as len(stringname) 

str_length = len(mydetails) 
print('Lenght of the string is : ', str_length)

#for x in range(str_length):
#    print(x)

i=0
for x in range(len(mydetails)):
    print(mydetails[i])
    i += 1
    #print(i)

# the above example we mentioned is to make u clear on the for loop and displaying the value in string array one by one, 
# now lets see another code, where use for loop to iterate through the string 
#
