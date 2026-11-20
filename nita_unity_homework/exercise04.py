print("===== MENU =====")

menu = {
    "Espresso": 1.20,
    "Macchiato": 1.50,
    "Cappuccino": 2.00,
    "Tea": 1.00,
    "Croissant": 1.80
}

menu["Cappuccino"] = 2.20
menu["Hot Chocolate"] = 2.50

for product, price in menu.items():
    print(f"{product}: {price:.2f} EUR")

print("================")

order = {}

for i in range(1, 5):
    product = input(f"Item {i}: ")

    if product in menu:
        quantity = int(input(f"Quantity of {product}: "))

        if product in order:
            order[product] = order[product] + quantity
        else:
            order[product] = quantity
    else:
        print(f"Sorry, {product} is not on the menu.")

print("===== RECEIPT =====")

total = 0

for product, quantity in order.items():
    price = menu[product]
    item_total = price * quantity
    total = total + item_total

    print(f"{product} x{quantity} = {item_total:.2f} EUR")

print("-------------------")

different_items = len(order)

print(f"Different Items: {different_items}")
print(f"Total: {total:.2f} EUR")

if total >= 10:
    discount = total * 0.10
else:
    discount = 0

to_pay = total - discount

print(f"Discount: {discount:.2f} EUR")
print(f"To Pay: {to_pay:.2f} EUR")
print("===================")