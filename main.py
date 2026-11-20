import json

def add_income(balance, income):
    if income.isdigit():
        int_income = int(income)
    else:
        print(f"Please enter the positive number! Thanks.")
        return balance
    if income.isdigit() and int_income > 0:
        balance += int_income
        print("Added.")
        return balance
    else:
        print(f"Please enter the positive number! Thanks.")
        return balance

def add_expense(balance, outcome):
    if outcome.isdigit():
        int_outcome = int(outcome)
    else:
        print(f"Invalid amout!")
        return balance

    if int_outcome <= balance and int_outcome > 0:
        balance -= int(outcome)
        print("The money has been deducted.")
        return balance
    else:
        print(f"Invalid amout!")
        return balance

def add_transactions(transactions, type, amount):
    if type == "income" and str(amount).isdigit() and int(amount) > 0:
        transactions.append({"type": type, 'amount': amount})
        return transactions
    elif type == "outcome" and str(amount).isdigit() and int(amount) > 0:
        transactions.append({"type": type, 'amount': amount})
        return transactions
    else:
        print("Invalid!")
        return transactions

def show_transactions(transactions):
    if not transactions:
        print("No transactions yet.")
        return
    print("Your transactions:")
    for number, transaction in enumerate(transactions, start=1):
        print(f"{number}. {transaction["type"].capitalize()}: {transaction["amount"]}")

def save_transactions(transactions):
    with open("transactions.json", "w") as file:
        json.dump(transactions, file)

def calculate_balance(transactions):
    balance = 0
    for transaction in transactions:
        if transaction["type"] == "income":
            balance += int(transaction["amount"])
        else:
            balance -= int(transaction["amount"])
    return balance

def main():
    try:
        with open("transactions.json", "r") as file:
            transactions = json.load(file)
    except FileNotFoundError:
        transactions = []

    balance = calculate_balance(transactions)

    while True:
        cmd = input()
        if cmd == "1":
            income = input("Add income: ")
            old_balance = balance
            balance = add_income(balance, income)
            if old_balance < balance:
                add_transactions(transactions, "income", income)
                save_transactions(transactions)
            print(balance)
        elif cmd == "2":
            outcome = input("Add expense: ")
            old_balance = balance
            balance = add_expense(balance, outcome)
            if old_balance > balance:
                add_transactions(transactions, "outcome", outcome)
                save_transactions(transactions)
            print(balance)

        elif cmd == "3":
            print(f"Your balance: {balance}")
        elif cmd == "4":
            show_transactions(transactions)
        elif cmd == "5":
            break
        else:
            print("Invalid option. Please enter the right option of the command. Thanks!")

main()
