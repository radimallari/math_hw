"""
1.) Write computer codes to compute the coefficients c_0, c_1,...,c_n and to 
evaluate the corresponding interpolation polynomial at an arbitrary point x. 
Test your code and turn in a run of your test. 
"""
from typing import List


def newton_coefficients(x: List[int], f_x: List[float]):
    """Finds the coefficients for Newton's interpolation form.
    :param x: List of nodes.
    :param f_x: List of values at x nodes.
    :return: List of coefficients used for Newton's interpolation polynomial.
    """
    n = len(x)
    c = []
    for i in range(n):
        c.append(f_x[i])

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
    """
    The evaluation of the interpolation polynomial in Newton's form can be done
    with the Horner-like scheme seen in class:

    p=c_n
    for j=n-1,n-2,...,0
        p=c_j+(x-x_j)*p;
    end
    """
    n = len(c) - 1
    p = c[n] + (x - x_j[n])
    for j in range(n - 1, -1, -1):
        p = (x - x_j[j]) * p + c[j]
    return p


def main():
    x = [5, 6, 9, 11]
    y = [12, 13, 14, 16]
    coeffs = newton_coefficients(x, y)
    print(interpolation_polynomial(7, x, coeffs))


main()
