import random
import string

def generate_alphanumeric_password(length, include_letters_and_numbers):
    '''
    Function to generate an alphanumeric password.

    Parameters:
        - length: Length of the password.
        - include_letters_and_numbers: Boolean value indicating whether to include letters and numbers in the password.

    Returns:
        - Generated password.
    '''
    if include_letters_and_numbers:
        # If include_letters_and_numbers is True, use both letters (lowercase and uppercase) and digits
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for _ in range(length))
    else:
        # If include_letters_and_numbers is False, use only digits
        characters = string.digits
        password = ''.join(random.choice(characters) for _ in range(length))
    return password


option = input('Enter [1] to generate a password with letters and numbers\nEnter [2] to generate a password with only numbers: \n-->')

if option == '1':
    length = int(input('Enter the length of the code: '))
    password = generate_alphanumeric_password(length, True)  # Generate password with letters and numbers
else:
    length = int(input('Enter the length of the code: '))
    password = generate_alphanumeric_password(length, False)  # Generate password with only numbers

print('Generated Password:', password)
