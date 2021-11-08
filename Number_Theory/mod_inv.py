from Number_Theory.optimized_gcd import *
import numpy as np

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

def matrix_mod_inv(matrix, n):
 #   if gcd(round(np.linalg.det(matrix)) % n, n) != 1:
 #      raise Exception('Mod inv does not exist. Gcd != 1')

    det = np.linalg.det(matrix)
    matrix_inv = np.linalg.inv(matrix) * det
    det = round(det) % n

    with np.nditer(matrix_inv, op_flags=['readwrite']) as it:
        for x in it:
            x[...] = int((np.matrix.round(x) * mod_inv(det,n)) % n)

    matrix_inv.astype(int)
    return matrix_inv






