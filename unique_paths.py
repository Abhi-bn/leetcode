def unique_paths(m, n):
    if m == 1 or n == 1:
        return 1

    return unique_paths(m - 1, n) + unique_paths(m, n - 1)


print(unique_paths(1, 3))
