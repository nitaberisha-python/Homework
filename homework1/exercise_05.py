store = input("Enter store name: ")

product1 = input("Enter first product name: ")
price1 = float(input("Enter first product price: "))
quantity1 = int(input("Enter first product quantity: "))

product2 = input("Enter second product name: ")
price2 = float(input("Enter second product price: "))
quantity2 = int(input("Enter second product quantity: "))

product3 = input("Enter third product name: ")
price3 = float(input("Enter third product price: "))
quantity3 = int(input("Enter third product quantity: "))

discount_percent = float(input("Enter discount percentage: "))

revenue1 = price1 * quantity1
revenue2 = price2 * quantity2
revenue3 = price3 * quantity3

gross_revenue = revenue1 + revenue2 + revenue3
total_products = quantity1 + quantity2 + quantity3

discount = gross_revenue * discount_percent / 100
revenue_after_discount = gross_revenue - discount

vat = revenue_after_discount * 18 / 100
final_revenue = revenue_after_discount + vat

average_revenue = final_revenue / total_products

print("DAILY SALES REPORT")
print("Store:", store)

print("Product 1:", product1)
print("Price:", price1)
print("Quantity:", quantity1)
print("Revenue:", revenue1)

print("Product 2:", product2)
print("Price:", price2)
print("Quantity:", quantity2)
print("Revenue:", revenue2)

print("Product 3:", product3)
print("Price:", price3)
print("Quantity:", quantity3)
print("Revenue:", revenue3)

print("Total Products Sold:", total_products)
print("Gross Revenue:", gross_revenue)
print("Discount:", discount)
print("Revenue After Discount:", revenue_after_discount)
print("VAT:", vat)
print("FINAL REVENUE:", final_revenue)
print("Average Revenue Per Item:", average_revenue)