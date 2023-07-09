# Vowel Count

# Collecting data
text = input('Enter any text: ').lower()
vowels = []

# Checking for vowels
if text.isdigit():
    print('No vowels were found in your text.')
else:
    for char in text:
        if char in 'aeiou':
            vowels.append(char)

# Displaying the results
print(f'Identified {len(vowels)} vowels - {vowels}')
print(f'The entered text was: {text}')
