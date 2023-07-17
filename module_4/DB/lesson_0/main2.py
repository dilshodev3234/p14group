
matrix = [

     [1, 2, 3],
     [1, 2, 3],
     [1, 2, 3]
]

c = 0
c += sum(matrix[0])
c += sum(matrix[-1])

for i in matrix[1:-1]:
    c += i[0]+i[-1]
print(c)





# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         print((row, col) , end=' ')
#     print()
# c = 0
# for i in range(len(matrix)):
#     c += matrix[i][i]
# print(c)
#
#
# print(sum([matrix[i][i] for i in range(len(matrix))]))







