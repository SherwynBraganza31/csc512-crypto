import optimized_gcd

def mod_inv(a, n):
    if not (optimized_gcd(a, n) == 1):
        raise ValueError("GCD of a and n should be 1")

    if a < 0:
        a = a + n

    if a > n:
        a = a % n

    inner_mod_inv(n, x, y)

def inner_mod_inv(n, x, y)


