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

def fermat_primality(p):
    if(p%2 == 0):
        return False

    for i in range(0, 30):
        temp = random.randint(2,p-2)
        if pow(temp, p-1, p) != 1:
            return False
    return True

def miller_rabin(p):
    # Test if P is 2 or even (odd primes only !)
    if p == 2 | p == 3:
        return True
    if(p%2 == 0):
        return False

    n = int(p)     # store the original value of p
    a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    for i in range(0, 5):
        a.append(random.randint(42, n -2))

    p = p - 1
    k = 0
    while (p % 2) == 0:
        p = p / 2
        k += 1
    # m = p since we've divided out 2 as a factor

    # for each witness in a, perform the test
    for i in range(0, len(a)):
        b = pow(a[i],int(p),n)
        #if b == 1 or b == -1:
        #   return True

        for i in range(1, k):
            b = pow(b, 2, n)
            if b == 1:
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


if __name__ == "__main__":
    main()




