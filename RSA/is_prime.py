##############################################################################
# This program uses the Fermat Primality Test to check if a number is Prime
# or not.
# Fermat Primality Test:
# A number is prime if for all 'a' belonging to [2, p-1], a^(p-1) gives you
# a 1.
#
#
# TODO Implement MILLER_RABIN
# TODO Implement SOLOVAY_STRASSEN
#############################################################################

from Number_Theory.jacobi import jacobi

def fermat_primality(p):
    for i in range(2, p - 1):
        if pow(i, p-1, p) != 1:
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
    return fermat_primality(p)
    #return solovay_strassen(p)

def main():
    p = int(input("Enter a non-even number to check for primality: "))
    print("The number is prime" if fermat_primality(p) else "The number is not-prime")


if __name__ == "__main__":
    main()




