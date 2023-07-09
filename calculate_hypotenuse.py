# Finding the Hypotenuse of a Right Triangle

# Collecting data
opposite_side = float(input('Length of the opposite side: '))
adjacent_side = float(input('Length of the adjacent side: '))

# Calculating the hypotenuse
hypotenuse = (opposite_side ** 2 + adjacent_side ** 2) ** 0.5

print(f'The hypotenuse is equal to {hypotenuse:.2f}')
