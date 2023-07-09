# Calculator with While Loop

# Summary: This code implements a calculator that can perform basic arithmetic operations using a while loop.

while True:
    # Inputting numbers and operator
    number_1 = input('Enter a number: ')
    number_2 = input('Enter another number: ')
    operator = input('Enter the operator (+ - * /): ')

    # Validating input numbers
    valid_numbers = None

    try:
        num_1_float = float(number_1)
        num_2_float = float(number_2)
        valid_numbers = True
    except:
        valid_numbers = None

    if valid_numbers is None:
        print('One or both of the numbers entered is invalid')
        continue

    # Validating operator
    valid_operators = '+-/*'

    if operator not in valid_operators:
        print('Invalid operator!')
        continue

    if len(operator) > 1:
        print('Enter only one operator')
        continue

    # Performing calculations
    if operator == '+':
        print(f'{num_1_float} + {num_2_float} = {num_1_float + num_2_float}')
    if operator == '-':
        print(f'{num_1_float} - {num_2_float} = {num_1_float - num_2_float}')
    if operator == '*':
        print(f'{num_1_float} * {num_2_float} = {num_1_float * num_2_float}')
    if operator == '/':
        try:
            print(f'{num_1_float} / {num_2_float} = {num_1_float / num_2_float}')
        except:
            print('You cannot divide a number by 0')

    # Exiting the calculator
    exit_choice = input('Do you want to exit? [Y]es: ').lower().startswith('y')

    if exit_choice is True:
        break
