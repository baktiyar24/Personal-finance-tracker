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