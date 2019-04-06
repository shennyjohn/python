fn = 'Joseph'
ln = 'John'

x = fn + '  ' +  ln 
daily_saving = 20
daily_parking = 10

salikamount = 12
daily_food = 8
# Find the yearly savings
# monthly saving muliply 12
monthly_saving = daily_saving*30
print("Your monthly saving is  ", monthly_saving)

# You are working 9 hours a day, so how much amount you spend during one hour for
# parking
working_hours = 9
per_hour_parking_charge = 10/9
# let us print it
print("Hourly you are spending this for parking ", per_hour_parking_charge)

# Now let us calculate the total expense in a month and in a year
# your expense will be Salik + parking + food +
#
daily_expense = daily_parking + salikamount + daily_food
print('Your daily expense is ', daily_expense)
print('Your monthly expense is',30*daily_expense)
print('Your early expense is',365*daily_expense)
"""
See this way of displaying print results
"""
print("See this way of displaying print results")
print("Your daily expense is %f" %(daily_expense))
print("Your monthly expense is  %d"  %(30*daily_expense))
print("Your early expense is %d" %(365*daily_expense))

# some multiplication with strings
print("You multiplied the name 3 times here", x*3)


# First we write it to the file

myexpense = open("myexpensefile.txt","w+")
myexpense.write("Your daily expense is %f \n" %(daily_expense))
myexpense.write("Your monthly expense is  %d  \n"  %(30*daily_expense))
myexpense.write("Your early expense is %d \n" %(365*daily_expense))

# we close the file
myexpense.close()

