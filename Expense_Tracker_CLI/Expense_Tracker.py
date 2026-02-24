def data_table(row,col):
    data_list = [[[]for _ in range(row)] for _ in range(col)]

    for i in range(col):
        for j in range(row):
            data_list[i][j]

    return data_list

def id_generator(row,col):
     id_list = [[[] for _ in range(row)] for _ in range(col)]

     for i in range(col):
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


row = 4
col = 4

list_0 = data_table(row,col)
list_1= id_generator(row,col)
day,month,year = ask_date()
list_2 = date_generator(row,col,day,month,year)
category = ask_category()
list_3 = category_setter(row,col,category)
amount = ask_amount()
list_4 = amount_recorder(row,col,amount)

for i in range(col):
    for j in range(row):
        list_0[i][0] = list_1[i][0]

for i in range(col):
    for j in range(row):
        list_0[col-1][1] = list_2[col-1][1]

for i in range(col):
    for j in range(row):
        list_0[col-1][2] = list_3[col-1][2]

for i in range(col):
    for j in range(row):
        list_0[col-1][3] = list_4[col-1][3]

print(list_0)