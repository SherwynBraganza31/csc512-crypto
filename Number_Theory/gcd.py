import sympy

##################################################################
# Function : factorize(a, n, factor_matrix)
# This function recursively divides a by n to get the largest
# multiple of n that is a divisor of a. It also checks if n is
# a prime factor because we only wanna account for prime factors
#
# In other words, repeatedly integer divides a by n, increasing
# the count of n as displayed in factor_matrix[n-1][1] by every
# time. The greatest divisor of a that is a multiple of only n
# is given by n ^ (factor_matrix[n-1][1])
#
# params : a - The number to be factored (int)
#        : n - The factor (int)
#        : factor_matrix - 2D matrix that holds the prime factors
#                          of a and the gcd of a that is a power
#                          of n.
#
# returns: nothing
#################################################################
def factorizer(a, n, factor_matrix):
    if a % n == 0 and sympy.isprime(n):  # replace with own isprime function
        factor_matrix[n-1][1] += 1
        factorizer(a//n, n, factor_matrix)
    return

##################################################################
# Function : gcd(x,y)
# Calculates the Greatest Common Divisor of x and y
#
# How the algorithm works:
# Find all the prime factors of x and y and their powers.
# GCD is set to 1 initially
# If any of x an y have common prime factors, multiply the GCD
# by the lower of the powers of the common prime factors.
#
# params : x - (int)
#        : y - (int)
#
# returns: (int) Greatest common divisor of x and y
#################################################################
def gcd(x, y):
    greatest_common_divisor = 1

########## Edge Case testing# #############
    if x == 0:
        raise ValueError("x cannot be 0")
    if y == 0:
        raise ValueError("y cannot be 0")

    if x < 0:
        x = abs(x)
    if y < 0:
        y = abs(y)

    if not isinstance(x, int):
        raise TypeError("x has to be an integer")
    if not isinstance(y, int):
        raise TypeError("y has to be an integer")


    # 1 is always a divisor of both x and y
    factor_matrix_x = [[1, 1]]     # matrix that contains the prime factors of x
    factor_matrix_y = [[1, 1]]     # matrix that contains the prime factors of y

    for i in range(2, x + 1):
        factor_matrix_x.append([i, 0])
        factorizer(x, i, factor_matrix_x)

    i = 2
    for i in range(2, y + 1):
        factor_matrix_y.append([i, 0])
        factorizer(y, i, factor_matrix_y)

    for i in range(0, len(factor_matrix_x) if len(factor_matrix_x) <= len(factor_matrix_y) else len(factor_matrix_y)):
        if factor_matrix_x[i][1] == 0 or factor_matrix_y[i][1] == 0:
            continue
        elif factor_matrix_x[i][1] <= factor_matrix_y[i][1]:
            greatest_common_divisor *= pow(factor_matrix_x[i][0], factor_matrix_x[i][1])
        else:
            greatest_common_divisor *= pow(factor_matrix_y[i][0], factor_matrix_y[i][1])

    return greatest_common_divisor



