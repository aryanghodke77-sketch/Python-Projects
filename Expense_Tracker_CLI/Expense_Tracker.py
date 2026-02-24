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

row = 4
col = 4

list_0 = data_table(row,col)
list_1= id_generator(row,col)

for i in range(col):
    for j in range(row):
        list_0[i][0] = list_1[i][0]

day,month,year = ask_date()
list_2 = date_generator(row,col,day,month,year)
for i in range(col):
    for j in range(row):
        list_0[col-1][1] = list_2[col-1][1]

print(list_0)