# Calculating Wall Area and Paint Quantity

# Head
title = 'Wall Area'
print('-'*50)
print(f'{title:^50}')
print('-'*50)

# Collecting data
width = float(input('Enter the width of your wall in meters: '))
height = float(input('Enter the height of your wall in meters: '))
print('-'*50)

# Calculating
area = width * height
paint_quantity = area / 2

# Displaying the data
print(f'Your wall measures {area} square meters.')
print(f'Therefore, you will need {paint_quantity} liters of paint.')
print('-'*50)
