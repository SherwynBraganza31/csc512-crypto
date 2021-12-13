import math
from RSA.is_prime import fermat_primality

def primitive_root(a, n):
    n = n-1
    factors = []

    for i in range(2, int(math.sqrt(n)) + 2):
        if not (fermat_primality(i)): # we only want to check prime factors
            continue
        if n % i == 0:
            factors.append(i)  # add to the factor list if its a factor

    for i in range(0, len(factors)):
        if ((a**i)%n) == 1:
            return False

    return True

def main():
    print("This program checks for if x is a primitive root mod n.")
    n = int(input("Enter in an 'n': "))
    x = int(input("Enter in an 'x': "))

    print(x, "is a primitive root mod" if primitive_root(x,n) else "is not a primitive root mod", n)

if __name__ == "__main__":
    main()
