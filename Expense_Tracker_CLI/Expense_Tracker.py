def data_table(row,col):
    data_list = [[[]for _ in range(row)] for _ in range(col)]

    for i in range(col):
        for j in range(row):
            data_list[i][j] = 0

    return data_list

def id_generator(row,col):
     id_list = [[[] for _ in range(row)] for _ in range(col)]

     for i in range(col):
        for j in range(row):
            id_list[i][0] = (i+1)
     
     return id_list

row = 3
col = 3

list1 = data_table(row,col)
list2 = id_generator(row,col)

for i in range(col):
    for j in range(row):
        list1[i][0] = list2[i][0]

print(list1)