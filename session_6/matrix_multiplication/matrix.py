matrix_a = [
    [10, 7, 9, 6, 5],
    [1, 3, 2, 4, 9],
    [7, 5, 8, 6, 2],
    [2, 1, 9, 3, 4],
    [3, 10, 1, 7, 8],
]

matrix_b = [
    [8, 2, 1, 9, 3],
    [4, 6, 7, 3, 5],
    [9, 2, 3, 8, 1],
    [1, 2, 4, 5, 7],
    [3, 6, 2, 1, 8],
]

result_matrix = []
for i in range(len(matrix_a)):
    row = []
    for j in range(len(matrix_b[0])):
        cell_sum = 0
        for k in range(len(matrix_b)):
            cell_sum += matrix_a[i][k] * matrix_b[k][j]
        row.append(cell_sum)
    result_matrix.append(row)

print("Matrix multiplication result:")
for row in result_matrix:
    print(row)
