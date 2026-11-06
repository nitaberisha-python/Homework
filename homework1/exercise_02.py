customer = input("Enter customer name: ")
product = input("Enter product name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount percentage: "))
shipping = float(input("Enter shipping cost: "))

subtotal = price * quantity
discount = subtotal * discount_percent / 100
price_after_discount = subtotal - discount
total_before_vat = price_after_discount + shipping
vat = total_before_vat * 18 / 100
total = total_before_vat + vat

print("ORDER INVOICE")
print("Customer:", customer)
print("Product:", product)
print("Unit Price:", price)
print("Quantity:", quantity)
print("Subtotal:", subtotal)
print("Discount:", discount)
print("Shipping:", shipping)
print("VAT:", vat)
print("TOTAL:", total)