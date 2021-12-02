import math
import random

def fermat_factorization(n):
    i = 1
    temp = math.sqrt(n + pow(i, 2))

    while temp != int(temp):
        i += 1
        temp = math.sqrt(n + pow(i, 2))

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


#print(square_bin_search)
print(fermat_factorization(1344340957))
#print(fermat_factorization(4897))
#print(fermat_factorization_nlogn(4897))