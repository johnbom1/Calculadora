operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

if operation == '+':
    print(f'{number_1} + {number_2} = ',number_1 + number_2) 

elif operation == '-':
    print(f'{number_1} - {number_2} = ',number_1 - number_2)

elif operation == '*':
    print(f'{number_1} * {number_2} = ',number_1 * number_2)

elif operation == '/':
    print(f'{number_1} / {number_2} = ',number_1 / number_2)

else:
    print('You have not typed a valid operator, please run the program again.')
