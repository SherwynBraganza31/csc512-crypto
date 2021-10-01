#############################################################
# Function : gcd(a,b)
# This function calculates the gcd of x and y and returns it
#
# It implements the Euclidean gcd algorithm
#
# @params : x - (int) One of the 2 numbers to calc the gcd
#           y - (int) One of the 2 numbers to calc the gcd
#
# @returns : (int) The gcd
#
#############################################################
def gcd(y, x):

    # Error checking and edge case testing
    if x == 0:
        raise ValueError("x cannot be 0")
    if y == 0:
        raise ValueError("y cannot be 0")

    if x < 0:
        x = abs(x)
    if y < 0:
        y = abs(y)

    if not isinstance(x, int):
        raise TypeError("x has to be an integer")
    if not isinstance(y, int):
        raise TypeError("y has to be an integer")

    # swap around if x > y
    if x > y:
        temp = y
        y = x
        x = temp

    return inner_gcd(x, y)

# The recursive portion of the gcd cycle.
def inner_gcd(x, y):
    if x == 0:
        return y
    return inner_gcd(y % x, x)

#def inner_ex_gcd(a, x, y)
#    if x == 0:
#       return (y, 0, 1)
#
#    inv, x, y = inner_ex_gcd(x, )
