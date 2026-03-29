# Expense Tracker (Python CLI)

## Overview

This is a **command-line Expense Tracker** built in Python using basic OOP concepts. It allows users to **add, edit, delete, and view expenses** with unique transaction IDs and date/category information.

The program stores all data in memory while it runs. It uses a simple **global ID counter** to assign unique IDs to each transaction.

---

## Features

* Add an expense with:

  * Date (day/month/year)
  * Category (e.g., Food, Rent, Entertainment)
  * Amount
* Edit an existing expense by its **transaction ID**
* Delete an expense by its **transaction ID**
* Display all recorded expenses in a table format
* Input validation for:

  * Numeric amounts
  * Proper day/month values

---

## How It Works

1. When you start the program, a menu is displayed with options to:

   1. Add expense
   2. Edit expense
   3. Delete expense
   4. Show all expenses
   5. Exit
2. Adding an expense:

   * User is prompted to enter a date, category, and amount.
   * The program assigns a unique ID automatically.
3. Editing or deleting requires the **ID of the transaction**.
4. The program loops until the user chooses **Exit**.

---

## Code Structure

* **`Tracker` class**: Handles all expense management

  * `add_expense(amount)` – Adds a new expense
  * `edit_expense()` – Edits an existing expense
  * `delete_expense()` – Deletes an expense by ID
  * `show_expenses()` – Displays all expenses
  * `get_date()`, `get_category()`, `get_amount()` – Handles user input
  * `id_generator()` – Generates unique IDs
* **Main program loop**: Presents a menu and calls appropriate methods.

---

## Usage

1. Run the program using Python 3:

   ```bash
   python expense_tracker.py
   ```
2. Follow the on-screen instructions to manage your expenses.

---

## Example Session

```
---- Operations you can perform ----
1. Add expenses
2. Edit expense
3. Delete expense
4. Show Expenses
5. Exit

Enter a number: 1

---- Add expenses ----
Enter the day: 12
Enter the month: 3
Enter the year: 2026
Enter the category: Food
Enter the Amount: 500
Added Expense ID 1

---- Operations you can perform ----
...
```
