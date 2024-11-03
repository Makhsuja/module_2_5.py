def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix
result = get_matrix(2, 2, 10)
result_2 = get_matrix(3, 3, 20)
result_3 = get_matrix(4, 4, 30)
print(result, result_2, result_3)
