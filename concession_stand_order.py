'''
You and three friends are going to a baseball game and offer to go to the concession stand for everyone. Each of them orders something, and you do too. Nachos and Pizza cost $6.00. A Cheeseburger meal costs $10.00. Water costs $4.00 and Coca-Cola costs $5.00. The tax rate is 7%.
'''

# Prices
water = 4.00
coca = 5.00
tax = 0.07
cheeseburger_meal = 10.00
pizza = 6.00
nachos = 6.00
total_cost = 0

# Order list
order = []

# Placing orders
while True:
    item = input('What is your order? We have:\n - Popcorn\n - Coca-Cola\n'
                 '- Pizza\n - Cheeseburger\n - Nachos\n - Water\n -->').lower()
    order.append(item)

    continue_order = int(input('Would you like anything else?\n [1] Yes\n [2] No\n-> '))
    if continue_order == 2:
        break

for item in order:
    if item == 'popcorn':
        print("We don't have popcorn, I got you a Coca-Cola.")
        total_cost = total_cost + coca
    if item == 'pizza':
        total_cost += pizza
    if item == 'cheeseburger':
        total_cost += cheeseburger_meal
    if item == 'water':
        total_cost += water
    if item == 'coca':
        total_cost += coca

# Calculating the final cost including tax
final_cost = total_cost + (total_cost * tax)

# Displaying the final order and total cost
print('ORDER')
print('-'*10)
for item in order:
    print(item)
print('-'*10)
print('Total to pay:')
print(final_cost)
