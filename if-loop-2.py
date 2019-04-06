#! /usr/bin/python3
income = input('Enter the income :')
expense = input('Enter the expense :')
print(type(income))
print(type(expense))
income = int(income)
expense = int(expense)
print('After casting string to int',type(income))
print('After casting string to int',type(expense))

if income > expense:
    print('Good work, you saved this much amount', income-expense)
elif income < expense:
    print('Be carefully, you are in debt of such amount', expense-income)
else:
    print('You just made it')

#Here you learned how to cast string to int, conditional statement (if loop) 
