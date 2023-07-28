# mat = [
#     [1, 1],
#     [0, 1]
# ]
# target = [
#     [1, 1],
#     [1, 0]
# ]

# re = []
# for _ in range(len(mat) - 1):
#     for i in list(zip(*mat)):
#         re.append(list(i[::-1]))
#     print(re)
#     mat = re.copy()
#     re = []

# print(mat == target)


# for _ in range(4):
#     if mat == target:
#         print(True)
#     mat = [list(i) for i in zip(*mat[::-1])]
# return False
