# Make a 2D Array

row_num=int(input("Enter row"))
col_num=int(input("Enter col"))

matrix = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        matrix[row][col]=row*col
print(matrix)

