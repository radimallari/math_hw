"""
4.) Write a code to compute a natural spline S(x) which interpolates a
collection of given points (x0, y0),(x1, y1), ··· ,(xn, yn) where
x0 < x1 < ··· < xn (do not assume they are equidistributed). Your code
should have a  triadiagonal solver for the resulting linear system of
equations (you’re not allowed to use Matlab’s operator to solve the linear
system).
"""
from typing import List

from matplotlib import pyplot as plt


def tridiagonal_matrix_solver(a, b, c, d):
    n = len(a)
    # Initialize variables
    m, l, u, y, x = [], [], [], [], [0 for i in range(n + 1)]

    m.append(a[0])
    for j in range(0, n):
        l.append(c[j - 1] / m[j - 1])
        u.append(b[j - 1])
        m.append(a[j] - l[j - 1] * b[j - 1])

    # Forward substitution
    y.append(d[0])
    for j in range(0, n):
        y.append(d[j] - l[j - 1] * y[j - 1])

    # Backward substitution
    for j in range(n, -1, -1):
        if j == n:
            x[j] = y[j] / m[j]
            continue
        x[j] = (y[j] - b[j] * x[j + 1]) / m[j]
    return x


def natural_cubic_spline_coeffs(x: List[int], y: List[int]):
    n = len(x)
    h = [x[i + 1] - x[i] for i in range(n - 1)]
    matrix_a_coeffs = [2 * (h[i] + h[i + 1]) for i in range(n - 2)]
    matrix_b_coeffs = matrix_c_coeffs = [h[i] for i in range(n - 2)]
    matrix_d_coeffs = []

    for i in range(n - 2):
        matrix_d_coeffs.append(
            -6 / h[i] * (y[1] - y[0]) + 6 / h[i + 1] * (y[i + 2] - y[i - 1])
        )

    z = tridiagonal_matrix_solver(
        matrix_a_coeffs, matrix_b_coeffs, matrix_c_coeffs, matrix_d_coeffs
    )

    polynomial_coeffs = []
    for j in range(n - 2):
        a_j = 1 / h[j] * (z[j + 1] - z[j])
        b_j = z[j] / 2
        c_j = 1 / h[j] * (y[j + 1] - y[j]) - (h[j] / 6 * (z[j + 1] + 2 * z[j]))
        d_j = y[j]
        polynomial_coeffs.append((a_j, b_j, c_j, d_j))
    return polynomial_coeffs


def main():
    # b_n = [6, 7, 8, 9]
    # a_n = [1, 2, 3, 4, 5]
    # c_n = [4, 5, 6, 7]
    # d_n = [10, 11, 12, 13, 14]
    # tridiagonal_matrix_solver(a_n, b_n, c_n, d_n)

    x = [0, 1, 3, 6, 8, 12]
    y = [5, 8, 12, 44, 60, 87]
    # x = [0, 1, 2, 3, 4, 5]
    # y = [12,14,22,39,58,77]
    n = len(x)
    coeffs = natural_cubic_spline_coeffs(x, y)

    for i in range(n - 2):
        print(
            f"S_0({i}<x<={i + 1}) = {coeffs[i][0]} + {coeffs[i][1]} (x-"
            f"{x[i]})+ {coeffs[i][2]} (x-{x[i]})^2+ {coeffs[i][3]} (x-"
            f"{x[i]})^3"
        )
    """
    5.) Use the values in Table 1 to construct a smooth parametric 
    representation of a curve passing through the points (xj , yj ), j = 0, 
    1, ..., 8 by finding the two natural cubic splines interpolating and 
    (tj , yj ), j = 0, 1, ..., 8, respectively. Tabulate the coefficients of 
    the splines and plot the resulting parametric curve.
    
    j       t_j     x_j      y_j
    0        0      1.5      0.75
    1      0.618    0.9      0.9
    2      0.935    0.6      1.0
    3      1.255    0.35     0.8
    4      1.636    0.2      0.45
    5      1.905    0.1      0.2
    6      2.317    0.5      0.1
    7      2.827    1.0      0.2
    8      3.330    1.5      0.25
    """
    # Cubic spline of (x_j, y_j) for j = 0, ..., 8
    print("Cubic spline of (x_j, y_j) for j = 0, ..., 8")
    x = [1.5, 0.9, 0.6, 0.35, 0.2, 0.1, 0.5, 1.0, 1.5]
    y = [0.75, 0.9, 1.0, 0.8, 0.45, 0.2, 0.1, 0.2, 0.25]
    n = len(x)
    coeffs_xj_yj = natural_cubic_spline_coeffs(x, y)
    for i in range(n - 2):
        print(
            f"S_0({i}<x<={i + 1}) = {coeffs_xj_yj[i][0]} + "
            f"{coeffs_xj_yj[i][1]} (x-{x[i]})+ {coeffs_xj_yj[i][2]} (x-"
            f"{x[i]})^2+ {coeffs_xj_yj[i][3]} (x-{x[i]})^3"
        )

    # Cubic spline of (t_j, y_j) for j = 0, ..., 8
    print("\n\nCubic spline of (t_j, y_j) for j = 0, ..., 8")
    y = [0.75, 0.9, 1.0, 0.8, 0.45, 0.2, 0.1, 0.2, 0.25]
    t = [0, 0.618, 0.935, 1.255, 1.636, 1.905, 2.317, 2.827, 3.330]
    n = len(t)
    coeffs_tj_yj = natural_cubic_spline_coeffs(t, y)
    for i in range(n - 2):
        print(
            f"S_0({i}<t<={i + 1}) = {coeffs_tj_yj[i][0]} + "
            f"{coeffs_tj_yj[i][1]} (t-{t[i]})+ {coeffs_tj_yj[i][2]} (t-"
            f"{t[i]})^2+ {coeffs_tj_yj[i][3]} (t-{t[i]})^3"
        )

    y = [0.75, 0.9, 1.0, 0.8, 0.45, 0.2, 0.1, 0.2, 0.25]
    t = [0, 0.618, 0.935, 1.255, 1.636, 1.905, 2.317, 2.827, 3.330]
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.plot(t, y)
    fig.show()


main()
