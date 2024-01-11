def calculate_discount(original_price, discount_percentage):
    discounted_price = original_price - (original_price * discount_percentage / 100)
    return discounted_price
#Here, We defined the function to calculate the discounted price. After the Calculation is done, the function will return the result i.e. Discounted Price.

original_price = float(input("Enter the Price: Rs. "))
discount_percentage = 10
discounted_price = calculate_discount(original_price, discount_percentage)
#Here, We have given the Original Price and with the function calculate_discount, the Discounted Price is calculated.

print("Original Price: Rs.", original_price)
print("Discounted Price: Rs.", discounted_price)
#This prints the Original and Discounted Price.

if discounted_price<50:
    print("Low-cost item")
elif discounted_price>=50 and discounted_price<100:
    print("Moderate-cost item")
else:
    print("High-cost item")
#Here, the Value of the item is printed depending on the price of the item after the discout has applied.
