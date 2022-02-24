"""
1.) Write computer codes to compute the coefficients c_0, c_1,...,c_n and to 
evaluate the corresponding interpolation polynomial at an arbitrary point x. 
Test your code and turn in a run of your test. 
"""
import math
from typing import List


def newton_coefficients(x: List[float], f_x: List[float]):
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


def interpolation_polynomial(x: float, x_j: List[float], c: List[float]):
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


def main():
    x = [1, 3, 5, 8]
    y = [1, 4, 16, 32]

    coeffs = newton_coefficients(x, y)
    print(coeffs)
    print(interpolation_polynomial(7, x, coeffs))

    # consider f(x) = xe^{-x^{2}} for x in [-1, 1]
    # with nodes x_j = -1 + j(2/10) for j = 0, 1, ..., 100
    f = lambda x: x * math.e ** ((-x) ** 2)
    x_j = [-1 + j * (2 / 10) for j in range(11)]
    f_x = [f(x) for x in x_j]
    p_10_coeffs = newton_coefficients(x_j, f_x)
    print(p_10_coeffs)

    # evaluate p_10_coeffs(x) at points x^{bar} = -1 + j(2/10) for j = 0, 1,
    # ..., 100
    x_j = [-1 + j * (2 / 100) for j in range(101)]
    f_x = [f(x) for x in x_j]
    p_100_coeffs = newton_coefficients(x_j, f_x)
    print(p_100_coeffs)

    # plot error f(x) - p_100_coeffs(x)
    error = []
    for x in x_j:
        print(x)
        error.append(f(x) - interpolation_polynomial(x, x_j, p_100_coeffs))
    print(error)

    """
    2.) Obtain the Hermite interpolation polynomial corresponding to the data
    f(0) = 0, f'(0) = 0, f(1) = 2, f'(1) = 3.
    """
    print("""
    In order to do this we first find our coefficients given by:
    
    x_j         0th         1st                                  2nd                                       3rd
     0        f(0)=0   f[0,0]=f'(0)/1=0             f[0,0,1]=(f[0,1]-f[0,0])/(1-0)=2     f[0,0,1,1]=(f[0,1,1]-f[0,0,1])/(1-0)=-1          
     0        f(0)=0   f[0,1]=(f(1)-f(0))/(1-0)=2   f[0,1,1]=(f[1,1]-f[0,1])/(1-0)=3
     1        f(1)=2   f[1,1]=f'(1)/1=3
     1        f(1)=2
    
    Then using the Newton interpolation polynomial:
    p_k(x)=f(x_0)+f[x_0,x_1](x-x_0)+...+f[x_0,x_1,...,x_k](x-x_0)...(x-x_k-1)
    we can obtain
    p_3(x)=f(0)+f[0,0](x-x_0)+f[0,0,1](x-x_0)(x-x_1)+f[0,0,1,1](x-x_0)(x-x_1)(x-x_2)
          =0+0(x-0)+2(x-0)(x-0)+(-1)(x-0)(x-0)(x-1)
          =2x^(2)+(-1)x^(3)-x^(2)
          =-x^(3)+x^(2)
    """)

    """
    3.) In class, we learned to use piecewise cubic splines that interpolate a 
    function. Find a piecewise linear function that interpolates 
    (0, 2), (1, 2),(2, 1),(3, 9).
    """
    print("""
    A piecewise linear function, say f(x), that interpolates the points is:
          /  x+2 for 0<x<=1
    f(x)= | -x+3 for 1<x<=2
          \ 3x-5 for 2<x<=3
    """)

    """
    4.) Write a code to compute a natural spline S(x) which interpolates a 
    collection of given points (x0, y0),(x1, y1), ··· ,(xn, yn) where
    x0 < x1 < ··· < xn (do not assume they are equidistributed). Your code 
    should have a  triadiagonal solver for the resulting linear system of 
    equations (you’re not allowed to use Matlab’s operator to solve the linear
    system).
    """


main()
