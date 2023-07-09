# Calculate Discounted Price

# Input data
original_price = float(input('Enter the product price: \n€'))
discount = float(input('Enter the discount percentage: \n'))

# Calculating discounts
percentage = discount / 100
discount_amount = original_price * percentage
final_price = original_price - discount_amount

print(f'The price with a discount of {discount:.1f}% is €{final_price:.2f}')
