
number_of_products = int(input("How many products? "))
has_card = input("Loyalty card? yes/no: ")

subtotal = 0
total_items = 0
expensive_products = 0

for i in range(1, number_of_products + 1):
    name = input(f"Product {i} name: ")
    price = float(input(f"Product {i} price: "))
    quantity = int(input(f"Product {i} quantity: "))

    line_total = price * quantity

    subtotal += line_total
    total_items += quantity

    if price >= 20:
        expensive_products += 1

    print(f"  {name} x{quantity} = {line_total:.2f} EUR")

if subtotal >= 100 and has_card == "yes":
    discount_percent = 15
elif subtotal >= 100 or has_card == "yes":
    discount_percent = 5
else:
    discount_percent = 0

discount = subtotal * discount_percent / 100
final_total = subtotal - discount

print("========== RECEIPT ==========")
print(f"Products: {number_of_products}")
print(f"Total Items: {total_items}")
print(f"Expensive Products (20+ EUR): {expensive_products}")
print(f"Subtotal: {subtotal:.2f} EUR")
print(f"Discount: {discount_percent}% (-{discount:.2f} EUR)")
print(f"Final Total: {final_total:.2f} EUR")
print("=============================")
