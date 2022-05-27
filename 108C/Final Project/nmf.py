import random
import numpy as np

from PIL import Image
from matplotlib import image as img, pyplot as plt
from pathlib import Path
from typing import List


def _grayscale_converter(img_file: Path):
    converted_image = Image.open(img_file).convert("L")
    converted_image.save(img_file.parent / img.name)


def _transpose(matrix_A: List[List]):
    return [list(x) for x in zip(*matrix_A)]


def nmf(A, k, r=25000, acceptable_error=0.01):
    """Factorizes matrix A to two matrices W and H

    :param A: List of rows representing some matrix
    :param k: number of features in factorization
    :param r: number of iterations
    :param acceptable_error:
    :return: number of iterations, calculated W and H matrix
    """
    # initialize W and H
    W = [[random.random() for _ in range(k)] for _ in range(len(A))]
    H = [[random.random() for _ in range(len(A[0]))] for _ in range(k)]

    # do not allow k values larger than the minimum of columns and rows
    if k > min([len(A), len(A[0])]):
        raise ValueError("k must be less than minimum of the dimensions of A")

    # iterate through until error is acceptable or number of specified iterations is reached
    end_iter, number_of_iters = False, 0
    while not end_iter and number_of_iters <= r:
        W_0, H_0 = W, H
        W_transpose, H_transpose = _transpose(W), _transpose(H)

        W = W * ((np.dot(A, H_transpose)) / np.dot(np.dot(W, H), H_transpose))
        H = H * ((np.dot(W_transpose, A)) / (np.dot(np.dot(W_transpose, W), H)))

        # calculate error between current iteration and previous
        W_error = np.linalg.norm(W - W_0, ord=2)
        H_error = np.linalg.norm(H - H_0, ord=2)

        print(f"{number_of_iters}.) W error: {W_error}, H error: {H_error}")
        number_of_iters += 1

        if W_error < acceptable_error and H_error < acceptable_error:
            end_iter = True

    # multiplicative update rule
    return number_of_iters, W, H


def main():
    file_name = "wow1.png"
    img_file = Path(__file__).resolve().parent / 'nmf_images' / file_name

    img_matrix = img.imread(img_file)
    number_of_iters, W, H = nmf(img_matrix, k=35)

    plt.imshow(W.dot(H), cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
