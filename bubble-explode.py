import copy


def explode_to_bottom(matrix):
    new_mat = copy.deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            count = 0
            li = []
            if j != len(matrix[i]) - 1 and matrix[i][j] == matrix[i][j+1]:
                count += 1
                li.append([i, j+1])
            if i != len(matrix) - 1 and matrix[i][j] == matrix[i+1][j]:
                count += 1
                li.append([i+1, j])
            if j != 0 and matrix[i][j] == matrix[i][j-1]:
                count += 1
                li.append([i, j-1])
            if i != 0 and matrix[i][j] == matrix[i-1][j]:
                count += 1
                li.append([i-1, j])
            if count >= 2:
                for x, y in li:
                    new_mat[x][y] = 0
                new_mat[i][j] = 0

    for j in range(len(new_mat[i])):
        k = len(new_mat) - 2
        l = len(new_mat) - 1
        if new_mat[l][j] == 0:
            while k >= 0:
                new_mat[l][j] = new_mat[k][j]
                if new_mat[k][j] != 0:
                    l -= 1
                new_mat[k][j] = 0
                k -= 1
    return new_mat


matrix = [[3, 1, 2, 1],
          [1, 1, 1, 4],
          [3, 1, 2, 2],
          [3, 3, 3, 4]]

if __name__ == '__main__':
    print(matrix)
    print(explode_to_bottom(matrix))
