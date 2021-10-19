#############################################################################
# Program that encrypts or decrypts a cipher according to the rules of
# using the Vignere Cipher Mechanism
# It has 2 modes:-
# a: Encryption Mode - Encrypts the plaintext with the provided key
# b: Decryption Mode - Decrypts the ciphertext with provided key
#
# Author: Sherwyn Braganza
#
# Date: 15 Oct 2021
#############################################################################

mode = 0
print("Modes:\n" +
      "a: Encryption Mode - Provide a plaintext and a key to encrypt it with. Prints out the ciphertext\n" +
      "b: Decryption Mode - Provide a ciphertext and the key. The program prints out the plaintext\n")

mode = input("Your choice: ")
print()
mode = mode[0]

if mode == "a":
    key = input("Enter the key:")
    plainText = input("Enter in plaintext:")

    # convert inputs into list elements
    plainText = list(str(plainText))
    key = list(str(key))

    # eliminate all empty spaces in the key or plaintext
    while True:
        try:
            plainText.remove(" ")
            key.remove(" ")
        except ValueError:
            break

    for i in range(0, len(plainText)):
        plainText[i] = chr((ord(plainText[i]) + ord(key[i % len(key)]) - 2*ord('a'))%26 + ord('a'))

    print(*plainText)

else:
    key = input("Enter the key:")
    cipherText = input("Enter in ciphertext:")

    # convert inputs into list elements
    cipherText = list(str(cipherText))
    key = list(str(key))

    while True:
        try:
            cipherText.remove(" ")
        except ValueError:
            break

    while True:
        try:
            cipherText.remove("")
        except ValueError:
            break

        while True:
            try:
                key.remove(" ")
            except ValueError:
                break

    for i in range(0, len(cipherText)):
        cipherText[i] = chr((ord(cipherText[i]) - ord(key[i % len(key)]))%26 + ord('a'))

    print(*cipherText)