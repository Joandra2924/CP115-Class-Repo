item_name = str(input("Enter item name: "))
item_price = float(input("Enter item price: "))

quantity = 3
tax_rate = 0.06

subtotal = float(item_price * quantity)
tax_amount = float(subtotal * tax_rate)
totalcost = float(subtotal + tax_amount)

print(f"subtotal: {subtotal}")
print(f"tax amount: {tax_amount}")
print(f"total cost: {totalcost}")