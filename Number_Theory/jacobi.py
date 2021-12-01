##################################################################
# Function : jacobi(a, n)
# This function calculates the value of the Jacobi Symbol - (a/n)
#
# The algorithm is borrowed from the website
# https://www.johndcook.com/blog/2019/02/12/computing-jacobi-symbols/
# and is based of the Jacobi Calculator Algorithm in
# Algorithmic Number Theory , Vol. 1: Efficient Algorithms (Foundations of Computing)
# by Eric Bach and Jeffrey Schallit
#
# params :
# returns: nothing
#################################################################
def jacobi(a, n):
    assert (n > a > 0 and n % 2 == 1)
    t = 1
    while a != 0:
        while a % 2 == 0:
            a /= 2
            r = n % 8
            if r == 3 or r == 5:
                t = -t
        a, n = n, a
        if a % 4 == n % 4 == 3:
            t = -t
        a %= n
    if n == 1:
        return t
    else:
        return 0