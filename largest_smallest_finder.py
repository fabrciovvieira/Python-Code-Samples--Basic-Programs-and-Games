# Finding the Largest and Smallest Numbers

# Collecting data
value_1 = int(input('Enter the first value: '))
value_2 = int(input('Enter the second value: '))
value_3 = int(input('Enter the third value: '))

# Checking values
largest = value_1
smallest = value_1

# Comparing values to find the largest and smallest
if value_2 > largest and value_2 > value_3:
    largest = value_2
elif value_3 > largest:
    largest = value_3

if value_2 < smallest and value_2 < value_3:
    smallest = value_2
elif value_3 < smallest:
    smallest = value_3

# Displaying the values
if largest == value_1:
    print(f'The largest value was the first one entered: {largest}')
elif largest == value_2:
    print(f'The largest value was the second one entered: {largest}')
elif largest == value_3:
    print(f'The largest value was the third one entered: {largest}')

if smallest < value_1 and smallest < value_2:
    print(f'The smallest value was the third one entered: {smallest}')
if smallest < value_2 and smallest < value_3:
    print(f'The smallest value was the first one entered: {smallest}')
if smallest < value_1 and smallest < value_3:
    print(f'The smallest value was the second one entered: {smallest}')
