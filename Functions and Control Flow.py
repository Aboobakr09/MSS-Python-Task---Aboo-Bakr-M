def calculate_discount(original_price, discount_percentage): #discount_percentage=10 to make it as a default parameter.
    discounted_price = original_price - (original_price * discount_percentage / 100) 
    return discounted_price
#Here, We defined the function to calculate the discounted price. After the Calculation is done, the function will return the result i.e. Discounted Price.

original_price = float(input("Enter the Price: Rs. ")) #Here, We are taking the input from the user.
discount_percentage = 10 #This is the default parameter. If we don't give the discount_percentage, it will take the default value as 10.
discounted_price = calculate_discount(original_price, discount_percentage) #Here, We are calling the function calculate_discount.
#Here, We have given the Original Price and with the function calculate_discount, the Discounted Price is calculated.

print("Original Price: Rs.", original_price)
print("Discounted Price: Rs.", discounted_price)
#This prints the Original and Discounted Prices.

if discounted_price<50:
    print("Low-cost item") #This prints the Value of the item depending on the price of the item after the discount has been applied.
elif discounted_price>=50 and discounted_price<100:
    print("Moderate-cost item")
else:
    print("High-cost item")
#Here, the Value of the item is printed depending on the price of the item after the discount has been applied.
