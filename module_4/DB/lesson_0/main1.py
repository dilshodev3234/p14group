# # # print(list(zip([1, 2, 3, 8], [4, 5, 6, 9])))
# # # list(map(lambda x : list(x), m a s s i v))
# #
# # grid = [
# #     [9, 9, 8, 1],
# #     [5, 6, 2, 6],
# #     [8, 2, 6, 4],
# #     [6, 2, 2, 2]
# # ]
# # re = []
# # for i in range(len(grid)-2):
# #     l = []
# #     for j in range(len(grid[0])-2):
# #         max_ = max([max(grid[k+i][j:j+3]) for k in range(3)])
# #         l.append(max_)
# #     re.append(l)
# # print(re)
# #
# from string import ascii_lowercase
#
# board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
# count = 0
# for i in range(len(board)):
#     for j in range(len(board[0])):
#         if board[i][j] == 'R':
#             row = i
#             col = j
#             break
#
# row_list = board[row]
# col_list = list(zip(*board))[col]
#
# r = ''.join(row_list).replace('.', '') # Rp
# c = ''.join(col_list).replace('.', '') # pRp
#
# i = r.index('R')
# count += 0 if i == 0 else r[i-1] in ascii_lowercase # left check
# count += 0 if i == len(r)-1 else r[i+1] in ascii_lowercase # right check
#
# i = c.index('R')
# count += 0 if i == 0 else c[i-1] in ascii_lowercase
# count += 0 if i == len(c)-1 else c[i+1] in ascii_lowercase
#
# print(count)
#
#
#
#
#
#
#
#
#
