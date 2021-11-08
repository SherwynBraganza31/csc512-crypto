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
from Number_Theory.mod_inv import matrix_mod_inv

# TODO Get user created matrix
ciphering_matrix = np.matrix('1 2 3; 4 5 6; 11 9 8')

# TODO Modular Matrix Inverse
ciphering_matrix_inv = matrix_mod_inv(ciphering_matrix, 26)
# ciphering_matrix_inv = np.matrix('22 5 1; 6 17 24; 15 13 1')

# TODO Calculate the number of rows and cols
col_width = 3


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

    # if the plainText is short of characters
    # in other words if length of plaintext % col_width != 0
    if len(plainText) % 3 != 0:
        for i in range(0, len(plainText) % col_width - 1):
            # append an arbitrary x
            plainText.append('x')

    for i in range(0, len(plainText), col_width):
        # formulate a 1x3 matrix (temp) s.t temp*cipher_matrix = ciphertext
        temp = []
        for j in range(0, col_width):
            temp.append(int(ord(plainText[i+j]) - ord('a')))
        temp = np.array(temp)   # convert temp into a numpy array
        temp = np.squeeze(temp)  # reshape temp into a n*n matrix where n = col_width
        temp = np.matmul(temp, ciphering_matrix)  # matrix multiplication
        temp = temp.tolist()  # convert temp to list
        for j in range(0, col_width):
            cipherText.append((int(temp[0][j]) % 26) + ord('a'))  # append it to the ciphertext

    print("Ciphertext = ", end="")
    for i in range(0, len(cipherText)):
        print(chr(cipherText[i]), end="")

####################### Decryption Mode ##########################
else:
    cipherText = input("Enter in the cipherText: ")
    cipherText = list(str(cipherText))
    plainText = []

    # loop to eliminate all spaces in the plaintext
    while True:
        try:
            cipherText.remove(" ")
        except ValueError:
            break

    for i in range(0, len(cipherText), col_width):
        # formulate a 1x3 matrix (temp) s.t temp*cipher_matrix_inv = plaintext
        temp = []
        for j in range(0, col_width):
            temp.append(int(ord(cipherText[i+j]) - ord('a')))
        temp = np.array(temp)  # convert temp into a numpy array
        temp = np.squeeze(temp)  # reshape temp into a n*n matrix where n = col_width
        temp = np.matmul(temp, ciphering_matrix_inv)  # matrix multiplication
        temp = temp.tolist()  # convert temp to a list
        for j in range(0, col_width):
            plainText.append((int(temp[0][j]) % 26) + ord('a'))  # append it to the plaintext vector

    print("Plaintext = ", end="")
    for i in range(0, len(plainText)):
        print(chr(plainText[i]), end="")