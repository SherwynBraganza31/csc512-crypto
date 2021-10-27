#############################################################################
# Program that encrypts or decrypts a cipher using the Block ciphering
# Mechanism
# A predetermined ciphering matrix is used:
#  1 2 3
#  4 5 6
# 11 9 8
#
# It has 2 modes:-
# a: Encryption Mode - Encrypts the plaintext with the provided keyword
# b: Decryption Mode - Decrypts the ciphertext with the provided keyword
#
# Author: Sherwyn Braganza
#
# TO-DO
# - Provide the user with the option to enter in the initial ciphering matrix
#
#
# Date: 27 Oct 2021
#############################################################################
from numpy.linalg import inv
import numpy as np

ciphering_matrix = np.matrix('1 2 3; 4 5 6; 11 9 8')
mode = 0
print("Modes:\n" +
      "a: Encryption Mode - Provide keyword and the plaintext. The program will encrypt the plaintext and display it.\n" +
      "b: Decryption Mode - Provide ciphertext and keyword. The program will decrypt the ciphertext and display the plaintext.\n")

mode = input("Your choice: ")
mode = mode[0]

####################### Encryption Mode ##########################
if mode == "a":
    plainText = input("Enter in the plaintext: ")

    plainText = plainText.lower()
    plainText = list(str(plainText))
    cipherText = []

    # loop to eliminate all spaces in the plaintext
    while True:
        try:
            plainText.remove(" ")
        except ValueError:
            break

    if len(plainText)%3 != 0:
        for i in range(0, len(plainText)%3 - 1):
            plainText.append('x')

    for i in range(0, len(plainText), 3):
        temp = []
        for j in range(0, 3):
            temp.append(int(ord(plainText[i+j]) - ord('a')))
        temp = np.array(temp)
        temp = np.squeeze(temp)
        temp = np.matmul(temp, ciphering_matrix)
        temp = temp.tolist()
        for j in range(0, 3):
            cipherText.append((int(temp[0][j]) % 26) + ord('a'))

    for i in range(0, len(cipherText)):
        print(chr(cipherText[i]), end="")

####################### Decryption Mode ##########################
else:
    cipherText = input("Enter in the cipherText: ")
    cipherText = list(str(cipherText))

    col_width = 3
    plainText = []

    # TODO Modular Matrix Inverse
    #ciphering_matrix_inv = inv(ciphering_matrix)
    ciphering_matrix_inv = np.matrix('22 5 1; 6 17 24; 15 13 1')

    # loop to eliminate all spaces in the plaintext
    while True:
        try:
            cipherText.remove(" ")
        except ValueError:
            break

    for i in range(0, len(cipherText), col_width):
        temp = []
        for j in range(0, col_width):
            temp.append(int(ord(cipherText[i+j]) - ord('a')))
        temp = np.array(temp)
        temp = np.squeeze(temp)
        temp = np.matmul(temp, ciphering_matrix_inv)
        temp = temp.tolist()
        for j in range(0, 3):
            plainText.append((int(temp[0][j]) % 26) + ord('a'))

    for i in range(0, len(plainText)):
        print(chr(plainText[i]), end="")