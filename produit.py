def multiply_matrices(mat1, mat2):
    row1 = len(mat1)
    col1 = len(mat1[0])
    col2 = len(mat2[0])

    result = [[0 for _ in range(col2)] for _ in range(row1)]

    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result

def display_matrix(mat):
    for row in mat:
        print(" ".join(map(str, row)))

mat1 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

mat2 = [[9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]]

result = multiply_matrices(mat1, mat2)

print("Matrix 1:")
display_matrix(mat1)

print("\nMatrix 2:")
display_matrix(mat2)

print("\nResultant Matrix:")
display_matrix(result)
