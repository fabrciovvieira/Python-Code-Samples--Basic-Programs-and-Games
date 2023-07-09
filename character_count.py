# Collecting data
text = input('Enter your text here: ')
character_count = {}

# Counting characters
for character in text:
    if character in character_count:
        character_count[character] += 1
    else:
        character_count[character] = 1

# Displaying character count
print('Character count:')
for character, count in character_count.items():
    if character == ' ':
        character = 'space'
    print(f'{character} : {count}')
