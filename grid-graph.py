import uuid
import random
m = 10
n = 10

grid = []
for i in range(m):
    grid.append(random.sample(range(0, 10000), m))

for i in range(m):
    print(grid[i])
tree_paths = {}
for i in range(m):
    data = []
    for j in range(n):
        vals = []
        if i != 0:
            vals.append(grid[i - 1][j])
        if i != m - 1:
            vals.append(grid[i + 1][j])
        if j != 0:
            vals.append(grid[i][j - 1])
        if j != n - 1:
            vals.append(grid[i][j + 1])
        tree_paths[grid[i][j]] = vals
print()
for k, v in tree_paths.items():
    print(k, ":", v)
