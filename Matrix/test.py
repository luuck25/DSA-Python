



matrix = [

[1,2,3],
[3,4,5]

]


# for row in matrix:
#     for val in row:
#         print(val,end =" ")


row_length = len(matrix)
col_length = len(matrix[0])

#Row wise traversal

print("### ROW WISE")
for row in range(row_length):
    for col in range(col_length):
        print(matrix[row][col],end= " ")
# column wise traversal
#         
print()
print("### COLUMN WISE")
for col in range(col_length):
    for row in range(row_length):
        print(matrix[row][col], end=" ")