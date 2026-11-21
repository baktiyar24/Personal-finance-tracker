from transactions import add_expense, add_income, add_transactions, show_transactions, calculate_balance
from storage import save_transactions, load_transactions

def main():
    transactions = load_transactions()
    balance = calculate_balance(transactions)

    while True:
        cmd = input()
        if cmd == "1":
            income = input("Add income: ")
            old_balance = balance
            if income.isdigit() and int(income) > 0:
                income = int(income)
                balance = add_income(balance, income)
            else:
                print(f"Please enter positive number. Thanks!")
            if old_balance < balance:
                add_transactions(transactions, "income", income)
                save_transactions(transactions)
            print(balance)
        elif cmd == "2":
            outcome = input("Add expense: ")
            old_balance = balance
            if outcome.isdigit() and int(outcome) > 0:
                outcome = int(outcome)
                balance = add_expense(balance, outcome)
            else:
                print(f"Please enter positive number. Thanks!")
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
