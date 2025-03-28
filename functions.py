#calculating discount
def calculate_discount(price, discount_percent):

    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

# prompt user fot input
original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))

# calculate the final price
final_price = calculate_discount(original_price, discount_percentage)
print(f"The final price after discount is: {final_price}")


