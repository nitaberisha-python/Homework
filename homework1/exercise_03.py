name = input("Enter your name: ")
salary = float(input("Enter monthly income: "))

rent = float(input("Enter rent: "))
food = float(input("Enter food expenses: "))
transport = float(input("Enter transport expenses: "))
internet = float(input("Enter internet expenses: "))
other = float(input("Enter other expenses: "))

total_expenses = rent + food + transport + internet + other
remaining = salary - total_expenses

spent_percent = total_expenses / salary * 100
remaining_percent = remaining / salary * 100

print("MONTHLY BUDGET")
print("Name:", name)
print("Monthly Income:", salary)
print("Rent:", rent)
print("Food:", food)
print("Transport:", transport)
print("Internet:", internet)
print("Other Expenses:", other)
print("Total Expenses:", total_expenses)
print("Remaining Money:", remaining)
print("Spent:", spent_percent, "%")
print("Remaining:", remaining_percent, "%")