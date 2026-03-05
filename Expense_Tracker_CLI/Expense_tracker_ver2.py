'''
Suggestions to reach L5:

Encapsulate table operations in a TransactionManager class.

Separate UI/input prompts from data operations.

Use a persistent or incremental transaction ID to avoid reuse after deletes.

Improve date validation using datetime module.

Enhance table display (alignment, zero-padded dates, totals, categories summary).

Add floating-point support for amounts.

Add confirm prompts for Delete/Edit to improve UX. '''


table = []

def id_generator():
    transaction_id = len(table) + 1
     
    return transaction_id

def ask_date():
    while True:
        try:
            day = int(input("Enter the day: "))
            month = int(input("Enter the month: "))
            year = int(input("Enter the year: "))
            if not (1 <= day <= 31 and 1 <= month <= 12):
                print("Invalid date! Try again.")
                continue
            else:
                break
        except ValueError:
            print("Please enter valid numbers")

    return day,month,year

def ask_category():    
    
    category = input(f"Enter the category: ")

    return category

def ask_amount():
    while True: 
        try:
            amount = int(input("Enter the Amount: "))
            return amount
        except ValueError:
            print("Please enter valid numbers")

def data_generator(transaction_id, day, month, year, category, amount):
    date = f"{day}/{month}/{year}"
    record = {"id": transaction_id,"date": date,"category": category,"amount": amount}
    
    return record

def UI_input(amount):
    day,month,year = ask_date()
    category = ask_category()
    transaction_id = id_generator()

    record = data_generator(transaction_id, day, month, year, category, amount)
    table.append(record)

    print("ID","\t","Date","\t","\t","Category","\t","amount")
    print(f'{record["id"]}\t{record["date"]}\t{record["category"]}\t\t{record["amount"]}')

def show_table():
    print("ID\tDate\t\tCategory\tAmount")
    for record in table:
        print(f'{record["id"]}\t{record["date"]}\t{record["category"]}\t{record["amount"]}')

while True:
    print("\n---- Operations you can perform ----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Edit")
    print("4. Delete")
    print("5. Show Expenses")
    print("6. Exit\n")

    try:
        choice = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid input")
        continue

    if choice == 1:
        print(f"\n---- Deposit ----\n")
        amount = ask_amount()

        UI_input(amount)

    elif choice == 2:
        print(f"\n---- Withdraw ----\n")
        amount = ask_amount()
        amount *= -1

        UI_input(amount)

    elif choice == 3:
        print(f"\n---- Edit ----\n")

        try:
            transaction_id = int(input("Write the ID of the Transaction : "))
        except ValueError:
            print("Please enter a valid input")
            continue

        for index, record in enumerate(table):
            if record["id"] == transaction_id:
                current_col = index
                break
        else:
            print("Transaction ID not found.")
            continue

        category = ask_category()
        amount = ask_amount()

        table[current_col]["category"] = category
        table[current_col]["amount"] = amount
        date = table[current_col]["date"]

        record = {"id": transaction_id,"date": date,"category": category,"amount": amount}
        
        print("ID","\t","Date","\t","\t","Category","\t","amount")
        print(f'{record["id"]}\t{record["date"]}\t{record["category"]}\t\t{record["amount"]}')
        print("\n")

    elif choice == 4:
        try:
            transaction_id = int(input("Enter the ID of the transaction to delete: "))
        except ValueError:
            print("Please enter a valid input")
            continue

        for index, record in enumerate(table):
            if record["id"] == transaction_id:
                table.pop(index)
                print("Transaction deleted.")
                break
        else:
            print("Transaction ID not found.")

    elif choice == 5:
        show_table()

    elif choice == 6:
        print("Exiting the program.")
        break