#############################################################################
# Program that encrypts or decrypts a cipher using the Vignere Ciphering
# Mechanism
# It has 2 modes:-
# a: Encryption Mode - Encrypts the plaintext with the provided key
# b: Decryption Mode - Decrypts the ciphertext with provided key
#
# Author: Sherwyn Braganza
#
# Date: 15 Oct 2021
#############################################################################
from freq_calc import get_freq

mode = 0
print("Modes:\n" +
      "a: Encryption Mode - Provide a plaintext and a key to encrypt it with. Prints out the ciphertext\n" +
      "b: Decryption Mode - Provide a ciphertext and the key. The program prints out the plaintext\n" +
      "c: Attack Mode - Provide ciphertext. The program will get the key, decrypt the ciphertext and display the plaintext.\n")


mode = input("Your choice: ")
print()
mode = mode[0]

################ Encryption Mode ###################
if mode == "a":
    key = input("Enter the key:")
    plainText = input("Enter in plaintext:")

    # convert inputs into list elements
    plainText = plainText.lower()
    plainText = list(str(plainText))
    key = list(str(key))

    # eliminate all empty spaces in the key or plaintext
    while True:
        try:
            plainText.remove(" ")
        except ValueError:
            break

    while True:
        try:
            key.remove(" ")
        except ValueError:
            break

    for i in range(0, len(plainText)):
        if plainText[i].isalpha():
            plainText[i] = chr((ord(plainText[i]) + ord(key[i % len(key)]) - 2*ord('a'))%26 + ord('a'))

    print(*plainText)


############### Decryption Mode ##################
elif mode == "b":
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

##################### Attack Mode #########################
else:
    cipherText = input("Enter in ciphertext:")
    cipherText = cipherText.lower()
    cipherText = list(str(cipherText))
    key = []

    while True:
        try:
            cipherText.remove(" ")
        except ValueError:
            break

    key_length = 0
    freq_matches = []
    for i in range(1, len(cipherText)):
        temp = []
        for j in range(0, (len(cipherText) - i)):
            if cipherText[j] == cipherText[i + j]:
                temp.append(cipherText[j])
        if len(temp) > len(freq_matches):
            freq_matches = temp
            key_length = i

    freq_matches = get_freq(str(freq_matches))

    for i in range(0, key_length):
        for j in (0, len(cipherText) - 2*key_length - i, key_length):
            if cipherText[j + i] == cipherText[j + key_length + i]:
                if cipherText[j+i] == chr(freq_matches[0][0]):
                    key.append(chr(ord(cipherText[j]) - 4 - ord('a')) % 26)
                elif cipherText[j+i] == chr(freq_matches[1][0]):
                    key.append(chr(ord(cipherText[j]) - 19 - ord('a')) % 26)

    print(*key)


