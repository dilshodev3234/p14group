from itertools import chain




mat = [[1, 2 , 3 , 4], [5, 6 , 7 , 8]]
r, c = 2, 4
l = [mat[i][j] for i in range(len(mat)) for j in range(len(mat[0]))]
print(l)
re = []
if len(l) == r*c:
    for i in range(r):
        re.append(l[i*c:i*c+c])
    print(re)
else:
    print(mat)



