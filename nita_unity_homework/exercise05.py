print("===== CLEANING =====")

orders = [
    {"id": 101, "city": "Vushtrri", "amount": 25.50, "status": "Delivered"},
    {"id": 102, "city": "Prishtinë", "amount": 40.00, "status": "Delivered"},
    {"id": 103, "city": "Mitrovicë", "amount": -10.00, "status": "Delivered"},
    {"id": 104, "city": "Vushtrri", "amount": 18.00, "status": "Cancelled"},
    {"id": 105, "city": "Prishtinë", "amount": 62.50, "status": "Delivered"},
    {"id": 102, "city": "Prishtinë", "amount": 40.00, "status": "Delivered"},
    {"id": 106, "city": "Mitrovicë", "amount": 33.00, "status": "Delivered"},
    {"id": 107, "city": "Vushtrri", "amount": 47.00, "status": "Delivered"}
]

seen_ids = []
clean_orders = []

duplicate_count = 0
invalid_count = 0
cancelled_count = 0

for order in orders:

    if order["id"] in seen_ids:
        print(f"Order {order['id']}: DUPLICATE - skipped")
        duplicate_count = duplicate_count + 1

    elif order["amount"] <= 0:
        print(f"Order {order['id']}: INVALID AMOUNT - skipped")
        invalid_count = invalid_count + 1
        seen_ids.append(order["id"])

    elif order["status"] == "Cancelled":
        print(f"Order {order['id']}: CANCELLED - skipped")
        cancelled_count = cancelled_count + 1
        seen_ids.append(order["id"])

    else:
        print(f"Order {order['id']}: OK")
        clean_orders.append(order)
        seen_ids.append(order["id"])


revenue_by_city = {}
orders_by_city = {}

for order in clean_orders:
    city = order["city"]
    amount = order["amount"]

    if city in revenue_by_city:
        revenue_by_city[city] = revenue_by_city[city] + amount
        orders_by_city[city] = orders_by_city[city] + 1
    else:
        revenue_by_city[city] = amount
        orders_by_city[city] = 1


print("===== REPORT BY CITY =====")

for city, revenue in revenue_by_city.items():
    number_of_orders = orders_by_city[city]
    average = revenue / number_of_orders

    print(f"{city}: {number_of_orders} orders | {revenue:.2f} EUR | avg {average:.2f} EUR")


total_revenue = 0

for amount in revenue_by_city.values():
    total_revenue = total_revenue + amount

best_city = ""
best_revenue = 0

for city, revenue in revenue_by_city.items():
    if revenue > best_revenue:
        best_revenue = revenue
        best_city = city

skipped_total = duplicate_count + invalid_count + cancelled_count

print("--------------------------")
print(f"Raw Orders: {len(orders)}")
print(f"Clean Orders: {len(clean_orders)}")
print(f"Skipped: {duplicate_count} duplicate, {invalid_count} invalid, {cancelled_count} cancelled")
print(f"Total Revenue: {total_revenue:.2f} EUR")
print(f"Best City: {best_city} ({best_revenue:.2f} EUR)")
print("==========================")