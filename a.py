balance = 0
while True:
    cmd = input()
    if cmd == "1":
        income = input("Add income: ")
        if income.isdigit() and int(income) > 0:
            balance += int(income)
            print("Added.")
        else:
            print(f"Please enter the positive number! Thanks.")
    elif cmd == "2":
        outcome = input("Add expense: ")
        if outcome.isdigit() and int(outcome) <= balance and int(outcome) > 0:
            balance -= int(outcome)
            print("The money has been deducted.")
        else:
            print(f"Invalid amout!")

    elif cmd == "3":
        print(f"Your balance: {balance}")
    elif cmd == "4":
        break
    else:
        print("Invalid option. Please enter the right option of the command. Thanks!")
