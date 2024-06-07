def matrix_multiplication(A, B): # Temporal O(n^3), Espacial O(n^2), con n := dimensión de A y B
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)] # Nuevo arreglo creado en memoria de dimensión n^2
    for i in range(n): # n iteraciones
        for j in range(n): # n * n = n^2 iteraciones
            for k in range(n): # n * n * n = n^3 iteraciones
                C[i][j] += A[i][k] * B[k][j]
    return C

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print(matrix_multiplication(A, B))
# Output: [[30, 24, 18], [84, 69, 54], [138, 114, 90]]
