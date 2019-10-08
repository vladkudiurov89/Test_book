def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j)
             for j in range(num_cols)]
            for i in range(num_rows)]


def is_diagonal(i, j):
    return 1 if i == j else 0


identity_matrix = make_matrix(5, 5, is_diagonal)
print(identity_matrix)

