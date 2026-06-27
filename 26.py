item1_price = float(input("Enter price of item 1: "))
item1_qty = int(input("Enter quantity of item 1: "))

item2_price = float(input("Enter price of item 2: "))
item2_qty = int(input("Enter quantity of item 2: "))

item3_price = float(input("Enter price of item 3: "))
item3_qty = int(input("Enter quantity of item 3: "))

total_bill = (item1_price * item1_qty) + (item2_price * item2_qty) + (item3_price * item3_qty)

print("\n--- Shopping Bill ---")
print("Item 1:", item1_price, "x", item1_qty, "=", item1_price * item1_qty)
print("Item 2:", item2_price, "x", item2_qty, "=", item2_price * item2_qty)
print("Item 3:", item3_price, "x", item3_qty, "=", item3_price * item3_qty)
print("Total Bill:", total_bill)
