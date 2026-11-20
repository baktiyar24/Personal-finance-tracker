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
            
def main():
    balance = 0
    transactions = []
    while True:
        cmd = input()
        if cmd == "1":
            income = input("Add income: ")
            old_balance = balance
            balance = add_income(balance, income)
            if old_balance < balance:
                add_transactions(transactions, "income", income)
            print(balance)
        elif cmd == "2":
            outcome = input("Add expense: ")
            old_balance = balance
            balance = add_expense(balance, outcome)
            if old_balance > balance:
                add_transactions(transactions, "outcome", outcome)
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
