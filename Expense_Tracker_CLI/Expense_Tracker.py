def data_table(row,col):
    data_list = [[[]for _ in range(row)] for _ in range(col)]

    for j in range(col):
        for i in range(row):
            data_list[j][i]

    return data_list

def id_generator(row,col):
     id_list = [[[] for _ in range(row)] for _ in range(col)]

     for j in range(col):
        for i in range(row):
            id_list[j][0] = (j+1)
     
     return id_list

row = 3
col = 3

h = data_table(row,col)
print(h)

l = id_generator(row,col)
print(l)  
