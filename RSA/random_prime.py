import random
from is_prime import is_prime

_LOWER_BOUND = 2
_UPPER_BOUND = 512

##############################################################################
# Asks for a number between 2 and 20 and finds a random prime number between
# 2^(n+1) - 1 and 2^(n) - 1.
#
# Uses the randint function from the random library to get a number between
# the two bounds. The number is then checked for primality using the most
# efficient primality testing algorithm implemented in the function is_prime
# and returns it if the number is prime or rerolls if its not
#############################################################################

def rando_prime(n, m):
    # get a random number between the range [n,m]. m <
    p = random.randint(n, m)
    past_non_primes = [p]

    # if p is not prime, increment p by 1
    while (not is_prime(p)) or p > m:
        p = p + 1

    return p

def main():
    n = int(input("Enter in a number between 2 and 256: "))

    while n < _LOWER_BOUND or n > _UPPER_BOUND:
        print("Number not within range. ", end="")
        n = int(input("Enter in a number between 2 and 256: "))
    print("A prime between (2^" + str(n+1) + " - 1) and (2^" + str(n) + " - 1) is: " + str(rando_prime(pow(2,n)-1, pow(2,n+1)-1)))


if __name__ == "__main__":
    main()