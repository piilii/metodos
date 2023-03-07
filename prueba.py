import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(- 100, 100, 10000)
y = 4 * x ** 3 + 1.2 * x ** 2 + 12
plt.figure(0)
plt.plot(x, y)
plt.title("Prueba entorno" )
plt.xlabel( "x" )
plt.ylabel( "y" )
plt.grid(True)
plt.show()

def reduce_matrix(m):
    # Funcion que implementa el algoritmo de Gauss-Jordan para la reduccion de una matriz
    matrix = m.copy()
    pivot_col = 0
    n_rows, n_cols = matrix.shape
    for row in range(n_rows):

        if pivot_col >= n_cols:
            return matrix

        row_pivot = row
        while matrix[row_pivot][pivot_col] == 0:
            row_pivot += 1
            if row_pivot == n_rows:
                row_pivot = row
                pivot_col += 1
                if n_cols == pivot_col:
                    return matrix
        matrix[row_pivot], matrix[row] = matrix[row], matrix[row_pivot]

        pivot = matrix[row][pivot_col]
        matrix[row] = [mrx / float(pivot) for mrx in matrix[row]]

        for other_row in range(n_rows):
            if other_row != row:
                below_pivot = matrix[other_row][pivot_col]
                matrix[other_row] = [iv - below_pivot * rv for rv, iv in zip(matrix[row], matrix[other_row])]
        pivot_col += 1
    return matrix