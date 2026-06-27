price = float(input("Enter the original price: "))
discount = float(input("Enter discount percentage: "))

discount_amount = (price * discount) / 100
final_price = price - discount_amount

print("\n--- Shopping Discount Calculator ---")
print("Original Price:", price)
print("Discount Percentage:", discount, "%")
print("Discount Amount:", discount_amount)
print("Final Price after Discount:", final_price)
