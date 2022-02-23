"""
1.) Write computer codes to compute the coefficients c_0, c_1,...,c_n and to 
evaluate the corresponding interpolation polynomial at an arbitrary point x. 
Test your code and turn in a run of your test. 
"""
import math
from typing import List


def newton_coefficients(x: List[int], f_x: List[float]):
    """Finds the coefficients for Newton's interpolation form.
    :param x: List of nodes.
    :param f_x: List of values at x nodes.
    :return: List of coefficients used for Newton's interpolation polynomial.
    """
    n = len(x)
    c = f_x
    for k in range(1, n):
        for j in range(n - 1, k - 1, -1):
            c[j] = (c[j] - c[j - 1]) / (x[j] - x[j - k])
    return c


def interpolation_polynomial(x: float, x_j: List[int], c: List[float]):
    """Uses Horner-like scheme to create Newton's polynomial.
    :param x: Point to evaluate the polynomial at
    :param x_j: List of nodes
    :param c: List of polynomial coefficients
    :return:
    """
    n = len(c) - 1
    p = c[n]

    for j in range(n, 0, -1):
        p = (x - x_j[j - 1]) * p + c[j - 1]
    return p


def func_to_interpolate(x):
    return x * math.e ** ((-x) ** 2)


def main():
    x = [1, 2, 3, 4]
    y = [1, 8, 27, 64]

    coeffs = newton_coefficients(x, y)
    print(coeffs)
    print(interpolation_polynomial(7, x, coeffs))

    """
    consider f(x) = xe^{-x^{2}} for x in [-1, 1] 
    with nodes x_j = -1 + j(2/10) for j = 0, 1, ..., 100
    """
    # evaluate p_10(x) at points x^{bar} = -1 + j(2/10) for j = 0, 1, ..., 100

    # plot error f(x) - p_10(x)


main()
