from functools import *
import math


def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors):
    return reduce(vector_add, vectors)


def scalar_multiply(c, v):
    return [c*v_i for v_i in v]


def vector_mean(vectors):
    length = len(vectors)
    return scalar_multiply(1/length, vector_sum(vectors))


def dot(v, w):
    return sum(v_i*w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v):
    return dot(v, v)


def magnitude(v):
    return math.sqrt(sum_of_squares(v))


def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))


def distance(v, w):
    return magnitude(vector_subtract(v, w))


def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols


def get_row(A, i):
    return A[i]


def get_column(A, j):
    return [A_i[j] for A_i in A]


def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j)
            for j in range(num_cols)]
            for i in range(num_rows)]


def is_diagonal(i, j):
    return 1 if i == j else 0


def mean(v):
    return sum(v)/len(v)


def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n//2

    if n % 2 == 1:
        return sorted_v[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2



