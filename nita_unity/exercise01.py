
balance = 280.0
correct_pin = "4321"
daily_limit = 300

pin = input("Enter PIN: ")

if pin == correct_pin:
    amount = float(input("Amount to withdraw: "))
    bank_atm = input("Is this your bank's ATM? yes/no: ")

    if bank_atm == "yes":
        fee = 0
    else:
        fee = 2.5

    if amount <= 0:
        print("Error: Invalid amount")
    elif amount > daily_limit:
        print("Error: Daily limit is 300 EUR")
    elif amount + fee > balance:
        print("Error: Insufficient funds")
    else:
        balance -= amount + fee

        print("===== RECEIPT =====")
        print(f"Withdrawn: {amount:.2f} EUR")
        print(f"Fee: {fee:.2f} EUR")
        print(f"New Balance: {balance:.2f} EUR")
        print("===================")

else:
    print("Wrong PIN. Card blocked.")
