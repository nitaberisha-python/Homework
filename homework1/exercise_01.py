name = input("Enter freelancer name: ")
hours = int(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))
bonus = float(input("Enter monthly bonus: "))
tax_percent = float(input("Enter tax percentage: "))

base_income = hours * rate
gross_income = base_income + bonus
tax = gross_income * tax_percent / 100
net_income = gross_income - tax

print("Freelancer Report")
print("Freelancer:", name)
print("Hours Worked:", hours)
print("Hourly Rate:", rate)
print("Base Income:", base_income)
print("Bonus:", bonus)
print("Gross Income:", gross_income)
print("Tax:", tax)
print("NET INCOME:", net_income)