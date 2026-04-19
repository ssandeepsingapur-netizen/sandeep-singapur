def add_matrices(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return "Matrices must have the same dimension for addiction"
    result = []
    for i in range (len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)
    return result

matrice1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrice2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
result = add_matrices(matrice1, matrice2)

if isinstance(result, str):
    print(result_matrice)
else:
    print("Result of matrix addiction:")
    for row in result:
        print(row)