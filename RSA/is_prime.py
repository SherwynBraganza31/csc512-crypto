##############################################################################
# This program uses the Fermat Primality Test to check if a number is Prime
# or not.
# Fermat Primality Test:
# A number is prime if for all 'a' belonging to [2, p-1], a^(p-1) gives you
# a 1.
#
# TODO Implement SOLOVAY_STRASSEN
#############################################################################
import random
from Number_Theory.jacobi import jacobi

def fermat_primality(p: int) -> bool:
    if p == 2:
        return True
    if p == 3:
        return True
    if p == 5:
        return True
    if(p%2 == 0):
        return False

    for i in range(0, 30):
        temp = random.randint(2, p-2)
        if pow(temp, p-1, p) != 1:
            return False
    return True

def miller_rabin(p: int) -> bool:
    # Test if P is 2 or even (odd primes only !)
    if p == 2:
        return True
    if(p%2 == 0):
        return False

    n = p     # store the original value of p
    # adding fixed set of witnesses as it guarantees primality upto 3,317,044,064,679,887,385,961,981
    a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]

    # adding a few random ints to make things spicy and as n is usually larger than 3,317,044,064,679,887,385,961,981
    for i in range(0, 20):
        a.append(random.randint(42, n -2))

    p = p - 1
    k = 0
    while (p % 2) == 0:
        p = p // 2
        k += 1
    # m = p since we've divided out 2 as a factor

    # for each witness in a, perform the test
    for i in range(0, len(a)):
        b = pow(a[i],p,n)
        if b == 1 or b == n-1:
            continue
        for j in range(1, k+1):
            b = pow(b, 2, n)
            if b == n-1:
                break
            if b == 1:
                return False
            if j == k :
                return False

    return True

def solovay_strassen(p):
    if p%2 == 0:
        return False
    for i in range(2, p-1):
        temp = int((p - 1)/2)
        if pow(i, temp, p) != 1:
            return False
    return True

def is_prime(p):
    #return fermat_primality(p)
    #return solovay_strassen(p)
    return miller_rabin(p)

def main():
    p = int(input("Enter a non-even number to check for primality: "))
    print("The number is prime by Fermat's " if fermat_primality(p) else "The number is not-prime by Fermat's")
    print("The number is prime by Miller-Rabin " if miller_rabin(p) else "The number is not-prime by Miller-Rabin")

def test_case(p):
    print("The number is prime by Fermat's " if fermat_primality(p) else "The number is not-prime by Fermat's")
    print("The number is prime by Miller-Rabin " if miller_rabin(p) else "The number is not-prime by Miller-Rabin")

if __name__ == "__main__":
    main()




