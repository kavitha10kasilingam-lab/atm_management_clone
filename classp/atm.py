# ATM / Banking System
# ===== ATM =====

# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Transfer
# 5. Transaction Summary
# 6. Change PIN
# 7. Exit
# Account number
# Customer name
# PIN
# Balance
# Deposit
# Withdrawal
# Transfer
# Balance validation
# PIN validation
# Transaction history
# Daily transaction limit
# Minimum balance
# Menu loop

# ===== ATM / BANKING SYSTEM =====

account = {
    "account_no": 123456789,
    "customer_name": "Kavitha",
    "pin": 1234,
    "balance": 10000
}

transactions = []

daily_limit = 20000
minimum_balance = 1000
daily_used = 0


# 1. Check Balance
def check_balance():
    print("\nCustomer Name:", account["customer_name"])
    print("Account Number:", account["account_no"])
    print("Available Balance: Rs.", account["balance"])


# 2. Deposit
def deposit():

    amount = int(input("Enter deposit amount: "))

    if amount <= 0:
        print("Enter a valid amount")

    else:
        account["balance"] = account["balance"] + amount

        transactions.append("Deposited Rs. " + str(amount))

        print("Amount deposited successfully")
        print("Current Balance:", account["balance"])


# 3. Withdraw
def withdraw():

    global daily_used

    amount = int(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Enter a valid amount")

    elif amount + minimum_balance > account["balance"]:
        print("Insufficient balance or minimum balance required")

    elif daily_used + amount > daily_limit:
        print("Daily transaction limit exceeded")

    else:
        account["balance"] = account["balance"] - amount

        daily_used = daily_used + amount

        transactions.append("Withdrawn Rs. " + str(amount))

        print("Please collect your cash")
        print("Remaining Balance:", account["balance"])


# 4. Transfer
def transfer():

    global daily_used

    receiver = int(input("Enter receiver account number: "))
    amount = int(input("Enter transfer amount: "))

    if receiver == account["account_no"]:
        print("Cannot transfer to your own account")

    elif amount <= 0:
        print("Enter a valid amount")

    elif amount + minimum_balance > account["balance"]:
        print("Insufficient balance")

    elif daily_used + amount > daily_limit:
        print("Daily transaction limit exceeded")

    else:
        account["balance"] = account["balance"] - amount

        daily_used = daily_used + amount

        transactions.append(
            "Transferred Rs. " + str(amount) +
            " to Account " + str(receiver)
        )

        print("Transfer successful")
        print("Remaining Balance:", account["balance"])


# 5. Transaction Summary
def transaction_summary():

    print("\n===== TRANSACTION HISTORY =====")

    if len(transactions) == 0:
        print("No transactions available")

    else:
        for transaction in transactions:
            print(transaction)

    print("Current Balance:", account["balance"])
    print("Daily Limit Used:", daily_used)
    print("Daily Limit Remaining:", daily_limit - daily_used)


# 6. Change PIN
def change_pin():

    old_pin = int(input("Enter old PIN: "))

    if old_pin == account["pin"]:

        new_pin = int(input("Enter new 4-digit PIN: "))

        if 1000 <= new_pin <= 9999:

            confirm_pin = int(input("Confirm new PIN: "))

            if new_pin == confirm_pin:
                account["pin"] = new_pin
                print("PIN changed successfully")

            else:
                print("PIN does not match")

        else:
            print("PIN must contain 4 digits")

    else:
        print("Incorrect old PIN")


# ===== PIN VALIDATION =====

print("===== WELCOME TO ATM =====")

attempts = 0
login = False

while attempts < 3:

    entered_pin = int(input("Enter your PIN: "))

    if entered_pin == account["pin"]:
        print("Login successful")
        login = True
        break

    else:
        attempts = attempts + 1
        print("Incorrect PIN")
        print("Attempts remaining:", 3 - attempts)


# ===== MAIN MENU =====

if login == True:

    while True:

        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction Summary")
        print("6. Change PIN")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            check_balance()

        elif choice == 2:
            deposit()

        elif choice == 3:
            withdraw()

        elif choice == 4:
            transfer()

        elif choice == 5:
            transaction_summary()

        elif choice == 6:
            change_pin()

        elif choice == 7:
            print("Thank you for using our ATM")
            break

        else:
            print("Invalid choice. Try again")

else:
    print("Your account is temporarily locked")
