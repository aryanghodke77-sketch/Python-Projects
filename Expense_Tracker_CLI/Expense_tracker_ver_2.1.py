'''
Suggestions to reach L5:

Encapsulate table operations in a TransactionManager class.

Separate UI/input prompts from data operations.

Use a persistent or incremental transaction ID to avoid reuse after deletes.

Improve date validation using datetime module.

Enhance table display (alignment, zero-padded dates, totals, categories summary).

Add floating-point support for amounts.

Add confirm prompts for Delete/Edit to improve UX.'''

import json

table = []
next_id = 1

# ------------------ ID Generator ------------------
def id_generator():
    global next_id
    transaction_id = next_id
    next_id += 1

    return transaction_id

# ------------------ User Inputs ------------------
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

# ------------------ Data Handling ------------------
def data_generator(transaction_id, day, month, year, category, amount):
    date = f"{day}/{month}/{year}"
    record = {"id": transaction_id,"date": date,"category": category,"amount": amount}
    
    return record

def create_record(amount):
    day,month,year = ask_date()
    category = ask_category()
    transaction_id = id_generator()

    record = data_generator(transaction_id, day, month, year, category, amount)
    table.append(record)
    save_file(table)

    print(f'{record["id"]}\t{record["date"]}\t{record["category"]}\t\t{record["amount"]}')

def delete_transaction():
    try:
        transaction_id = int(input("Enter the ID to delete: "))
    except ValueError:
        print("Invalid input")
        return

    for index, record in enumerate(table):
        if record["id"] == transaction_id:
            table.pop(index)
            save_file(table)
            print("Transaction deleted.")
            return

    print("Transaction ID not found.")

def edit_transaction():
    try:
        transaction_id = int(input("Write the ID of the Transaction : "))
    except ValueError:
        print("Please enter a valid input")
        return False

    current_col = None
    for index, record in enumerate(table):
        if record["id"] == transaction_id:
            current_col = index
            break
    if current_col is None:
        print("Transaction ID not found.")
        return False

    category = ask_category()
    amount = ask_amount()

    table[current_col]["category"] = category
    table[current_col]["amount"] = amount
    date = table[current_col]["date"]

    record = {"id": transaction_id,"date": date,"category": category,"amount": amount}
    table[current_col] = record
    save_file(table)

    return True

# ------------------ File Handling ------------------
def load_file():
    global table, next_id
    try:
        with open("database.txt","r") as data:
            table = json.load(data)
            if table:
                next_id = max(record["id"] for record in table) + 1
    except FileNotFoundError:
        table = []
    except json.JSONDecodeError:
        table = []

def save_file(updated_table):
    with open("database.txt","w") as data:
        json.dump(updated_table, data, indent = 4)

# ------------------ Display ------------------
def show_table():
    print("ID\tDate\t\tCategory\tAmount")
    for record in table:
        print(f'{record["id"]}\t{record["date"]}\t\t{record["category"]}\t{record["amount"]}')

# ------------------ Main Program ------------------

load_file()
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

        create_record(amount)

    elif choice == 2:
        print(f"\n---- Withdraw ----\n")
        amount = ask_amount() * -1

        create_record(amount)

    elif choice == 3:
        if edit_transaction():
            print("Transaction edited")
        else:
            print("Transaction invalid")

    elif choice == 4:
        delete_transaction()

    elif choice == 5:
        show_table()

    elif choice == 6:
        print("Exiting the program.")
        break

# ------------ END --------------