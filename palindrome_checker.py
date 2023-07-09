# Checking for Palindrome

# Collecting data
text = input('Enter your text: => ').upper()

# Checking if it is a palindrome
if text.replace(' ', '') == text[::-1].replace(' ', ''):
    print('Your text is a palindrome')
    print(f'{text} = {text[::-1]}')
    print('')
else:
    print(f'{text} is not a palindrome, {text[::-1]} is different from {text}')
