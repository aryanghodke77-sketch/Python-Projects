next_id = 1 

class Tracker:
    def __init__(self):
        self.expenses = []

# ------------------ User Inputs ------------------           
    def id_generator(self):
        global next_id
        transaction_id = next_id
        next_id += 1
        return transaction_id
        
    def get_date(self):
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
    
        return f"{day}/{month}/{year}"
        
    def get_category(self):    
        return input(f"Enter the category: ")
        
    def get_amount(self):
        while True: 
            try:
                amount = int(input("Enter the Amount: "))
                return amount
            except ValueError:
                print("Please enter valid numbers")

# ------------------ Data Handling ------------------
    def show_expenses(self):
        if not self.expenses:
            print("No expenses to show.")
            return
        print("ID\tDate\t\tCategory\tAmount")
        for record in self.expenses:
            print(f'{record["id"]}\t{record["date"]}\t\t{record["category"]}\t\t{record["amount"]}')

    def add_expense(self,amount):
        date = self.get_date()
        category = self.get_category()
        transaction_id = self.id_generator()
        self.expenses.append({"id": transaction_id,"date": date,"category": category,"amount": amount})
        
    def delete_expense(self):
        try:
            self.transaction_id = int(input("Write the ID of the Transaction : "))
        except ValueError:
            print("Please enter a valid input")
            return False
        
        for i, expense in enumerate(self.expenses):
            if expense["id"] == self.transaction_id:
                self.expenses.pop(i)
                print("Expense deleted.")
                return
        return False
        
    def edit_expense(self):
        try:
            self.transaction_id = int(input("Write the ID of the Transaction : "))
        except ValueError:
            print("Please enter a valid input")
            return False

        new_category = self.get_category()
        new_amount = self.get_amount()

        for i in self.expenses:
            if i["id"] == self.transaction_id:
                i["category"] = new_category
                i["amount"] = new_amount
                print("Expense updated.")
                return
        print("Expense ID not found.")
                   
# ------------------- Main ---------------------
expense = Tracker()

while True:
    
    print("\n---- Operations you can perform ----")
    print("1. Add expenses")
    print("2. Edit expense")
    print("3. Delete expense")
    print("4. Show Expenses")
    print("5. Exit\n")

    try:
        choice = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid input")
        continue

    if choice == 1:
        print(f"\n---- Add expenses ----\n")
        amount = expense.get_amount()
        expense.add_expense(amount)
        
    elif choice == 2:
        if expense.edit_expense():
            print("Transaction edited")
        else:
            print("Transaction invalid")
    
    elif choice == 3:
        if expense.delete_expense():
            print("Transaction deleted.")
        else:
            print("Transaction ID not found.")
            
    elif choice == 4:
        expense.show_expenses()

    elif choice == 5:
        print("Exiting the program.")
        break