# Welcome message and instruction

print("Welcome to AB's Calculator.")
print('Select an operator: ')
print(' + for Addittion')
print(' - for Substraction')
print(' * for Multiplication')
print(' / for Division')

# Getting the user input 

number_1 = float(input('First Number: '))
operator = input('Operator: ')
number_2 = float(input('Second Number: '))

# Performing calculation 

if operator == '+':
    print('Equation:', number_1, '+', number_2, '=', number_1 + number_2)

elif operator == '-':
    print('Equation:', number_1, '-', number_2, '=', number_1 - number_2)
    
elif operator == '*': 
     print('Equation:', number_1, '*', number_2, '=', number_1 * number_2)

elif operator == '/':
    if number_2 !=0:
        print('Equation:', number_1, '/', number_2, '=', number_1 / number_2)
    else:
        print('Error')

else: 
    print('Invalid operation')