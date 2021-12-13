from Number_Theory.optimized_gcd import *
import numpy as np

##################################################################
# Function : mod_inv
# Utilizes the extended gcd function defined in optimized_gcd.py
# to find the modular inverse of a mod(n) when a and n are
# relatively prime.
#
# Throws an error if a and n are not relatively prime.
#
# params : a - The number who's mod inverse needs to be found
#        : n - The mod number
#
# returns: nothing
#################################################################
def mod_inv(a, n):
    if a < 0:
        a = a + n

    if a > n:
       a = a % n

    g, x, y = inner_ex_gcd(a, n)
    if g != 1:
        raise Exception('Mod inv does not exist because gcd != 1')
    else:
        return x % n

##################################################################
# Function : mod_inv
# Implements the mod inverse
#
# Throws an error if a and n are not relatively prime.
#
# params : matrix - The matrix who's mod inverse needs to be found
#        : n - The mod number
#
# returns: nothing
#################################################################
def matrix_mod_inv(matrix, n):
    det = np.linalg.det(matrix)
    matrix_inv = np.linalg.inv(matrix) * det
    det = round(det) % n

    with np.nditer(matrix_inv, op_flags=['readwrite']) as it:
        for x in it:
            x[...] = int((np.matrix.round(x) * mod_inv(det,n)) % n)

    matrix_inv.astype(int)
    return matrix_inv






