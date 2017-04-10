from random import randint

class Matrix:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.rows = []

        for i in range(m):
            self.rows.append([0]*n)

    def set(self, i, j, value):
        self.rows[i][j] = value

    def get(self, i, j):
        return self.rows[i][j]

    def remove_row(self, i):
        mat = Matrix(self.m - 1, self.n)

        for row in range(self.m):
            if row < i:
                mat.rows[row] = self.rows[row][:]
            elif row > i:
                mat.rows[row - 1] = self.rows[row][:]

        return mat

    def remove_col(self, j):
        mat = Matrix(self.m, self.n - 1)
        mat.rows = []

        for row in self.rows:
            row = row[:]
            row.pop(j)
            mat.rows.append(row)

        return mat

    def randomize(self):
        for row in self.rows:
            for j in range(len(row)):
                row[j] = randint(1, 9)

    def __str__(self):
        str_mat = ''

        for row in self.rows:
            str_mat += str(row)[1:-1].replace(',', ' ') + '\n'

        return str_mat

def det(mat):
    if mat.m and mat.n == 1: # base case, 1x1 matrix (basically a scalar)
        return mat.get(0, 0)
    else:
        d = 0
        for j in range(mat.n):
            d += (-1)**j * mat.get(0, j)*det(mat.remove_row(0).remove_col(j))

        return d

if __name__ == '__main__':
    mat = Matrix(9, 9)
    mat.randomize()
    print(mat)
    print('determinant =', det(mat))

