def transpose_matrix(matrix):
    row, cols = len(matrix), len(matrix[0])
    result =  [[0 for _ in range(row)] for _ in range(cols)]
    
    for i in range(row):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    
    return result
matrix = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]
]
transpose_matrix = transpose_matrix(matrix)
 
for row in transpose_matrix:
   print(row)
