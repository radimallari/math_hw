import random
import numpy as np
from typing import List


def _transpose(matrix_A: List[List]):
    return [list(x) for x in zip(*matrix_A)]


def _dot_product(matrix_A, matrix_B):
    return sum([i * j for i, j in zip(matrix_A, matrix_B)])


def nmf(A, k, r=10, threshold=0.01):
    """Factorizes matrix A to two matrices W and H

    :param A: List of rows representing some matrix
    :param k: number of features in factorization
    :param r: number of iterations
    :param threshold:
    :return:
    """
    # initialize W and H
    W = [[random.random() for _ in range(k)] for _ in range(len(A))]
    H = [[random.random() for _ in range(len(A[0]))] for _ in range(k)]

    if k > min([len(A), len(A[0])]):
        raise ValueError("k must be less than minimum of the dimensions of A")

    # iterate through
    W_0 = W
    H_0 = H
    W_transpose = _transpose(W)
    H_transpose = _transpose(H)

    # multiplicative update rule
    W = W * ((np.dot(A, H_transpose)) / np.dot(np.dot(W, H), H_transpose))
    H = H * ((np.dot(W_transpose, A)) / (np.dot(np.dot(W_transpose, W), H)))

    print(W)
    print(H)
    # minimize the Frobenius norm between A and W
    H_error = np.linalg.norm(H-H_0, ord=2)
    # minimize the Frobenius norm between A and H
    W_error = np.linalg.norm(W-W_0, ord=2)

some_matrix = [[12, 7, 6], [4, 5, 2]]
nmf(some_matrix, 2)
