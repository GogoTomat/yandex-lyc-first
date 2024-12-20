# table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(table[1][1])

# table = []
# for i in range(5):
#     row = [int(elem) for elem in input().split()]
#     table.append(row)
# print(table)
# print([[int(elem) for elem in input().split()] for i in range(5)])
# print([[0] * 10 for _ in range(10)])
# table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(3):
#     for j in range(3):
#         print(table[i][j], end='\t')
#     print()
# matrix = [[1, 2, 3],
#           [4, 5, 6]]
# print(matrix[0][2])
# rows = int(input())
# cols = int(input())

# table = []

# for _ in range(rows):
#     row = []
#     for _ in range(cols):
#         element = input()
#         row.append(element)
#     table.append(row)

# for row in table:
#     print('\t'.join(row) + '\t')
table = []
a = int(input())
for i in range(a):
    table.append(input().split(","))
a = int(input())
for i in range(a):
    b, c = input().split(",")
    print(table[int(b)][int(c)])

