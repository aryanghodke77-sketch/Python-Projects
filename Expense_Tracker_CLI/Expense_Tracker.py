def data_table(row,col):
    data_list = [[[]for _ in range(row)] for _ in range(col)]

    for j in range(col):
        for i in range(row):
            data_list[i][0].append(i+1)

    return data_list


row = 3
col = 3
sample_test = data_table(row,col)
print(sample_test)
