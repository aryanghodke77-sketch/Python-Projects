def data_table(row,col):
    data_list = [[[]for _ in range(row)] for _ in range(col)]

    return data_list

def id_generator(row,col):
     id_list = [[[] for _ in range(row)] for _ in range(col+1)]

     for i in range(col+1):
        for j in range(row):
            id_list[i][0] = (i+1)
     
     return id_list

def ask_date():    
    day = int(input("Enter the day: "))
    month = int(input("Enter the month: "))
    year = int(input("Enter the year: "))
    
    return day,month,year

def date_generator(row,col,day,month,year):
    date_list = [[[] for _ in range(row)] for _ in range(col)]
    date_list[col-1][1] = f"{day} | {month} | {year}"
    
    return date_list

def ask_category():    
    category = input(f"Enter the category: ")

    return category

def category_setter(row,col,category):
    category_list = [[[] for _ in range(row)] for _ in range(col)]
    category_list[col-1][2] = f"{category}"
    
    return category_list

def ask_amount():    
    amount = input(f"Enter the Amount: ")

    return amount

def amount_recorder(row,col,amount):
    amount_list = [[[] for _ in range(row)] for _ in range(col)]
    amount_list[col-1][3] = f"{amount}"
    
    return amount_list

def transaction(deposit,withdraw,row,col,day,month,year,category,amount):
    
    amount = int(amount)
    withdraw_amount = -abs(amount)
    
    list_0 = data_table(row,col)
    list_1= id_generator(row,col)
    list_2 = date_generator(row,col,day,month,year)
    list_3 = category_setter(row,col,category)
    list_4 = amount_recorder(row,col,amount)
    list_5 = amount_recorder(row,col,withdraw_amount)

    for i in range(col):
        for j in range(row):
            list_0[col-1][1] = list_2[col-1][1]

    for i in range(col):
        for j in range(row):
            list_0[col-1][2] = list_3[col-1][2]

    if deposit == 1:
        for i in range(col):
            for j in range(row):
                list_0[col-1][3] = list_4[col-1][3]
    if withdraw == 1:
        for i in range(col):
            for j in range(row):
                list_0[col-1][3] = list_5[col-1][3]

    return list_0

def UI_Transaction(deposit,withdraw,row,col):
    
    if deposit == 1:
        print(f"\n---- Deposit ----\n")
    else:
        print(f"\n---- withdraw ----\n")

    day,month,year = ask_date()
    category = ask_category()
    amount = ask_amount()

    print(transaction(deposit,withdraw,row,col,day,month,year,category,amount))

row = 4
col = 1

list_0 = data_table(row,col)
list_1= id_generator(row,col)
    
for i in range(col):
    for j in range(row):
        list_0[i][0] = list_1[i][0]

while True:
    print("---- Operations you can perform ----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Edit")
    print("4. Delete")
    print("5. Exit\n")

    choice = int(input("Enter choice : "))
    deposit, withdraw = (1, 0) if choice == 1 else (0, 1) if choice == 2 else (0, 0)

    if choice == 1 or choice == 2:
        UI_Transaction(deposit,withdraw,row,col)
        col += 1
        

