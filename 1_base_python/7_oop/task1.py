class Matrix:
    def __init__(self, new_matrix):
        self.matrix = new_matrix

    def __str__(self):
        view_matrix = ''
        for x, element in enumerate(self.matrix):
            for i, elm in enumerate(element):
                view_matrix += str(elm) + ' '
                if i+1 == len(element) and x+1 != len(self.matrix):
                    view_matrix += '\n'

        return view_matrix

    def __add__(self, matrix_2):
        if len(self.matrix) == len(matrix_2.matrix) and len(self.matrix[0]) == len(matrix_2.matrix[0]):
            new_matrix = []
            for x, element in enumerate(self.matrix):
                row_of_matrix = []
                for i, elm in enumerate(element):
                    row_of_matrix.append(self.matrix[x][i] + matrix_2.matrix[x][i])
                    if i + 1 == len(element):
                        new_matrix.append(row_of_matrix)
            return Matrix(new_matrix)
        else:
            return 'Невозможно сложить несоразмерные матрицы'


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[3, 4, 5], [8, 7, 6], [2, 5, 9]])
matrix_3 = matrix_1 + matrix_2
print(matrix_1)
print(matrix_2)
print(matrix_3)
