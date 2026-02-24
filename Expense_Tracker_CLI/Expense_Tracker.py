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
    a = int(input("Enter the day: "))
    b = int(input("Enter the month: "))
    c = int(input("Enter the year: "))
    
    return a,b,c

def date_generator(row,col,a,b,c):
    date_list = [[[] for _ in range(row)] for _ in range(col)]
    date_list[col-1][1] = f"{a} | {b} | {c}"
    
    return date_list

row = 4
col = 4

list_0 = data_table(row,col)
list_1= id_generator(row,col)

for i in range(col):
    for j in range(row):
        list_0[i][0] = list_1[i][0]

a,b,c = ask_date()
h = date_generator(row,col,a,b,c)
print(h)

list_2 = date_generator(row,col,a,b,c)
for i in range(col):
    for j in range(row):
        list_0[col-1][1] = list_2[col-1][1]

print(list_0)