import math
from random_prime import rando_prime
import random
from Number_Theory.optimized_gcd import gcd
from Number_Theory.mod_inv import mod_inv


def _RSA_encrypt(message, d, n):
    cipherText = []
    for i in range(0, len(message)):
        cipherText.append(pow(ord(message[i]),d,n))
    return cipherText

def _RSA_decrypt(message, e, n):
    plainText = []
    for i in range(0, len(message)):
        plainText.append(chr(pow(message[i], e, n) % 256))
    return "".join(plainText)

def main():
    p = rando_prime(pow(2, 127), pow(2,128))
    q = rando_prime(pow(2, 122), pow(2,123))
    n = p*q
    phi_n = (p-1) * (q-1)

    d = random.randint(2, phi_n - 1)
    while gcd(d, phi_n) != 1:
        d = random.randint(2, phi_n - 1)
    e = mod_inv(d, phi_n)

    plaintext = input("Enter in a message: ")
    cipherText = _RSA_encrypt(plaintext, d, n)

    readable_cipherText = []
    for i in range (0, len(cipherText)): readable_cipherText.append(chr(cipherText[i]%256))
    readable_cipherText = "".join(readable_cipherText)

    print("The cipherText is: ", readable_cipherText) # This has no significance but I just thought it would be cool!
    print("The plainText is: ", _RSA_decrypt(cipherText, e, n))


if __name__ == "__main__":
    main()

