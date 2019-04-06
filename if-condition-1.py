# coding: utf-8
#!/usr/bin/python
# Here we will see the if condition, take the case that you are comparing  your income and expenditure.
# the code compares the income and expenditure, if income is more, it will say “Good work, you saved this much amount “,
# If expenditure is more it should display “Be carefully, you are in debt of such amount.
#If  the income and expenditure is same, it should say “You just made it”

#see this code:- it will not work as you expected

income = input('Enter the income  :')
expense = input('Enter the expense :')

print('Ha ha this code is not going to work as u expected')
print('It has some thing to do with string to integer conversion')
print('We learned last class, rectify it ')
if income > expense:
    print('Good work, you saved this much amount', income-expense)
elif income < expense:
    print('Be carefully, you are in debt of such amount', expense-income)
else:
    print('You just made it')
