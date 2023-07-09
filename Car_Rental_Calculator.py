# Collecting data from the user
qtd_days = int(input('How many days was the car rented for: \n=> '))
km_traveled = float(input('How many kilometers were traveled: \n=> '))

# Calculating the price
price_per_day = 60 * qtd_days  # Calculate the price based on the number of days
price_per_km = 0.15 * km_traveled  # Calculate the price based on the number of kilometers
total = price_per_day + price_per_km  # Calculate the total price

# Displaying the result
print(f'You rented the car for {qtd_days} day(s) and traveled a total of {km_traveled} km,\n'
      f'With a price of £60 per day and €0.15 per km\n\n'
      f'The total amount to be paid is €{total:.2f} ')
