# Generating CPF

import random

cpf = ''
counter = 0

# Generating the first 9 digits
while counter < 9:
    digit = random.randint(0, 9)
    cpf = cpf + str(digit)
    counter += 1

# Generating the 10th digit
digit_10_counter = 0
digit_10_sum = 0
for d in cpf:
    if digit_10_counter == 0:
        digit_10_sum = digit_10_sum + (int(d) * 10)  # Multiply the digit by the corresponding weight and sum the results
    elif digit_10_counter == 1:
        digit_10_sum = digit_10_sum + (int(d) * 9)
    elif digit_10_counter == 2:
        digit_10_sum = digit_10_sum + (int(d) * 8)
    elif digit_10_counter == 3:
        digit_10_sum = digit_10_sum + (int(d) * 7)
    elif digit_10_counter == 4:
        digit_10_sum = digit_10_sum + (int(d) * 6)
    elif digit_10_counter == 5:
        digit_10_sum = digit_10_sum + (int(d) * 5)
    elif digit_10_counter == 6:
        digit_10_sum = digit_10_sum + (int(d) * 4)
    elif digit_10_counter == 7:
        digit_10_sum = digit_10_sum + (int(d) * 3)
    elif digit_10_counter == 8:
        digit_10_sum = digit_10_sum + (int(d) * 2)
    digit_10_counter += 1

digit_10 = digit_10_sum % 11  # Calculate the remainder of the division by 11

# Generating the 11th digit
digit_11_counter = 0
digit_11_sum = 0

if digit_10 == 0 or digit_10 == 1 or digit_10 == 10 or digit_10 == 11:
    cpf = cpf + '0'  # If the remainder is 0, 1, 10, or 11, append 0 as the 10th digit
else:
    digit_10 = 11 - digit_10  # Otherwise, subtract the remainder from 11
    cpf = cpf + str(digit_10)

for d in cpf:
    if digit_11_counter == 0:
        digit_11_sum = digit_11_sum + (int(d) * 10)  # Multiply the digit by the corresponding weight and sum the results
    elif digit_11_counter == 1:
        digit_11_sum = digit_11_sum + (int(d) * 9)
    elif digit_11_counter == 2:
        digit_11_sum = digit_11_sum + (int(d) * 8)
    elif digit_11_counter == 3:
        digit_11_sum = digit_11_sum + (int(d) * 7)
    elif digit_11_counter == 4:
        digit_11_sum = digit_11_sum + (int(d) * 6)
    elif digit_11_counter == 5:
        digit_11_sum = digit_11_sum + (int(d) * 5)
    elif digit_11_counter == 6:
        digit_11_sum = digit_11_sum + (int(d) * 4)
    elif digit_11_counter == 7:
        digit_11_sum = digit_11_sum + (int(d) * 3)
    elif digit_11_counter == 8:
        digit_11_sum = digit_11_sum + (int(d) * 2)
    elif digit_11_counter == 9:
        digit_11_sum = digit_11_sum + (int(d) * 1)
    digit_11_counter += 1

digit_11 = digit_11_sum % 11  # Calculate the remainder of the division by 11

if digit_11 == 0 or digit_11 == 1 or digit_11 == 10 or digit_11 == 11:
    digit_11 = 11 - digit_11  # If the remainder is 0, 1, 10, or 11, subtract the remainder from 11
    cpf = cpf + '0'
else:
    digit_11 = 11 - digit_11  # Otherwise, subtract the remainder from 11
    cpf = cpf + str(digit_11)

cpf_separated = ''

# Creating a formatting for easy visualization
for digit in cpf:
    if len(cpf_separated) == 3:
        cpf_separated = cpf_separated + '.' + digit  
    elif len(cpf_separated) == 7:
        cpf_separated = cpf_separated + '.' + digit  
    elif len(cpf_separated) == 11:
        cpf_separated = cpf_separated + '-' + digit  
    else:
        cpf_separated = cpf_separated + digit

print(f'Your CPF is: {cpf_separated}') #Explaining the CPF generation code:

'''
- The CPF (Cadastro de Pessoas Físicas) is a unique identification number used in Brazil.
- The code uses random number generation to create the first 9 digits of the CPF.
- The 10th digit is calculated based on the weighted sum of the first 9 digits.
- The 11th digit is calculated similarly to the 10th digit, taking into account the previously calculated digits.
- The CPF is formatted with dots and a hyphen to follow the standard format in Brazil.
- The generated CPF is printed as the output.

Summary: The CPF is an identification number used in Brazil. This code generates a random CPF by calculating the check digits based on the weighted sum of the other digits. The resulting CPF is formatted and displayed as the output.
'''