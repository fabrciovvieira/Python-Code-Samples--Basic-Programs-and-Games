'''
 B - BASAL
 M - METABOLIC
 R - RATE

 FOR MEN:
BMR = 10 * weight (kg) + 6.25 * height (cm) - 5 * age (year) + 5

FOR WOMEN:
BMR = 10 * weigth (kg) + 6.25 * height (cm) - 5 * age (year) - 161
 '''


print('-' * 50)
print('{:^50}'.format(' - BASAL METABOLIC RATE CALCULATION - '))
print('-' * 50)

name = input('What is your name? ')
age = int(input(f'How old are you, {name}? '))
height_str = input('How tall are you?(cm) ').replace(',.', '')
weight_str = input('How heavy are you? ').replace(',', '.')

height_float = float(height_str)
weight_float = float(weight_str)

while True: 
    gender = input('What is your gender ?\n[ F ] - Female\n[ M ] - Male\n-->  ').upper()
    if gender == 'F':
        bmr = 10 * weight_float + 6.25 * height_float - 5 * age - 161
        break
    elif gender == 'M':
        bmr = 10 * weight_float + 6.25 * height_float - 5 * age + 5
        break
    else:
        print('Invalid value entered, please enter only F or M')


print(f'Your daily Basal Metabolic Rate (BMR) is {bmr} calories per day ')

