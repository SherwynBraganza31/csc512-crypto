import math
import random
import itertools
from Number_Theory.optimized_gcd import gcd
from is_prime import is_prime

def fermat_factorization(n):
    if math.sqrt(n) == int(math.sqrt(n)):
        return math.sqrt(n), math.sqrt(n)

    i = 1
    temp = math.sqrt(n + i**2)

    while temp != int(temp) and i < 2**22:
        i += 1
        temp = math.sqrt(n + i**2)

    if i >= 2**20:
        return "MAXED OUT"
    else:
        return int(temp+i), int(temp-i)

def fermat_factorization_nlogn(n):
    temp = n
    power = 0
    i = 0

    while power == 0:
        i += 1
        temp = n + math.pow(i,2)
        power = square_bin_search(temp)

    return power-i, power+i

def square_bin_search(number):
    upper_bound = pow(2, 128)
    lower_bound = 1
    found_square = 0

    while (upper_bound != lower_bound) and (pow(found_square,2) != number):
        found_square = random.randint(lower_bound, upper_bound)
        if pow(found_square, 2) > number:
            upper_bound = found_square
        if pow(found_square, 2) < number:
            lower_bound = found_square

    if pow(found_square, 2) == number:
        return found_square
    else:
        return 0

def pollard_p1(n):
    B = int(math.sqrt(n))
    a = 2
    d = n
    b = a

    # if n%2 == 0:
    #     return 2, n//2

    while d == n:
        for i in range(1, B):
            b = (b**i)%n

        if b - 1 != 0:
            d = gcd(n, b-1)
        else:
            d = n
            b = 2
        # d = math.gcd(n, b - 1)
        if d == 1:
            return n, 1
        elif d == n:
            B = B//2

    return d, n//d

def pollard_rho(n):
    x = 1
    for i in itertools.count():
        y = x
        for i in range (2**i):
            x = (x*x + 1) % n
            factor = math.gcd(abs(x-y), n)
            if factor > 1:
                return factor, n//factor

#def universal_factorization(n):



def test_cases():
    # print("For number: 1344340957\n", "Fermat Factorization = ", fermat_factorization(1344340957), \
    #       "\nPollard P-1 Factorization = ", pollard_p1(1344340957), "\nPollard Rho = ", pollard_rho(1344340957), end="\n\n")

    a = [42647, 51826]

    for i in range(0,len(a)):
        p = a[i]
        if is_prime(p):
            print("For number: ", p,  "\nFermat Factorization = ", (1,p),
                  "\nPollard P-1 Factorization = ", pollard_p1(p), "\nPollard Rho Factorization = ", pollard_rho(p), end="\n\n")
        else:
            print("For number: ", p,  "\nFermat Factorization = ", fermat_factorization(p),
                  "\nPollard P-1 Factorization = ", pollard_p1(p), "\nPollard Rho Factorization = ", pollard_rho(p), end="\n\n")

    for i in range(0,10):
        p = random.randint(2**8, 2**16)
        if is_prime(p):
            print("For number: ", p,  "\nFermat Factorization = ", (1,p),
                  "\nPollard P-1 Factorization = ", pollard_p1(p), "\nPollard Rho Factorization = ", pollard_rho(p), end="\n\n")
        else:
            print("For number: ", p,  "\nFermat Factorization = ", fermat_factorization(p),
                  "\nPollard P-1 Factorization = ", pollard_p1(p), "\nPollard Rho Factorization = ", pollard_rho(p), end="\n\n")

if __name__ == "__main__":
    test_cases()
#print(square_bin_search)
#print(fermat_factorization(1344340957))

