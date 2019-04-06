#    The below code will not work as you expected, Why because the values interred are stored as strings


income = input('Enter the income : ')
expense = input('Enter the expense : ')

if income > expense:
    print('Good work, you saved this much amount  :', income-expense)
elif income < expense:
    print('Be carefully, you are in debt of such amount  :', expense-income)
else:
    print('You just made it')
#    The above code will not work as you expected, Why because the values interred are stored as strings

