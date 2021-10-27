#############################################################################
# Program that encrypts or decrypts a cipher using the ADFGX ciphering
# Mechanism
# A predetermined ADFGX matrix is used:
#    A  D  G  F  X
#    -------------
# A| p  g  c  e  n
# D| b  q  o  z  r
# G| s  l  a  f  t
# F| m  d  v  i  w
# X| k  u  y  x  h
#
#
# It has 2 modes:-
# a: Encryption Mode - Encrypts the plaintext with the provided keyword
# b: Decryption Mode - Decrypts the ciphertext with the provided keyword
#
# Author: Sherwyn Braganza
#
# TO-DO
# - Provide the user with the option to enter in the initial ADFGX matrix
#
#
# Date: 26 Oct 2021
#############################################################################

from operator import itemgetter

# preset adfgx matrix
adfgx_matrix = [['p', 'g', 'c', 'e', 'n'],
                ['b', 'q', 'o', 'z', 'r'],
                ['s', 'l', 'a', 'f', 't'],
                ['m', 'd', 'v', 'i', 'w'],
                ['k', 'u', 'y', 'x', 'h']]

# TO-DO ask user to input adfgx matrix

adgfx = ['a', 'd', 'f', 'g', 'x']

# encoder - relates the alphabet to their corresponding ADFGX encoding
encoder = [0] * 26
encoder = list(encoder)
for i in range(0, 5):
    for j in range(0, 5):
        encoder[ord(adfgx_matrix[i][j]) - ord('a')] = (str(adgfx[i])+str(adgfx[j]))

# i = j as per ADFGX rules
encoder[9] = encoder[8]



mode = 0
print("Modes:\n" +
      "a: Encryption Mode - Provide keyword and the plaintext. The program will encrypt the plaintext and display it.\n" +
      "b: Decryption Mode - Provide ciphertext and keyword. The program will decrypt the ciphertext and display the plaintext.\n")

mode = input("Your choice: ")
mode = mode[0]

####################### Encryption Mode ##########################
if mode == "a":
    keyword = input("Enter in the keyword: ")
    plainText = input("Enter in the plaintext: ")

    plainText = plainText.lower()
    plainText = list(str(plainText))
    keyword = list(keyword)

    # loop to eliminate all spaces in the plaintext
    while True:
        try:
            plainText.remove(" ")
        except ValueError:
            break

    # place the encoded message into the keyword matrix
    for i in range(0, len(plainText)):
        if plainText[i].isalpha():
            keyword[2*i % len(keyword)] = keyword[2*i % len(keyword)] + encoder[ord(plainText[i]) - ord('a')][0]
            keyword[(2*i+1) % len(keyword)] = keyword[(2*i+1) % len(keyword)] + encoder[ord(plainText[i]) - ord('a')][1]

    # sort the keyword matrix in ascending order
    keyword = sorted(keyword, key=itemgetter(0))

    # print out the keyword matrix
    print("The cipher text is: ", end="")
    for i in range(0, len(keyword)):
        for j in range(1, len(keyword[i])):
            print(keyword[i][j].upper(), end="")



####################### Decryption Mode ##########################
else:
    keyword = input("Enter in the keyword: ")
    cipherText = input("Enter in the cipherText: ")

    cipherText = cipherText.lower()
    cipherText = list(str(cipherText))
    keyword = list(keyword)
    keyword_len = len(keyword)
    plainText = []

    # loop to eliminate all spaces in the plaintext
    while True:
        try:
            cipherText.remove(" ")
        except ValueError:
            break

    ord_keyword = sorted(keyword, key=itemgetter(0))

    for i in range(0, int(len(cipherText)/keyword_len) * keyword_len, keyword_len):
        for j in range(0, keyword_len):
            ord_keyword[int(i/keyword_len)] = ord_keyword[int(i/keyword_len)] + cipherText[i + j]

    for i in range(0, keyword_len):
        for j in range(0, keyword_len):
            if keyword[i][0] == ord_keyword[j][0]:
                keyword[i] = ord_keyword[j]

    for i in range(0, len(keyword), 2):
        for j in range(0, 26):
            if keyword[int(i/keyword_len)][i%keyword_len + 1] == encoder[j][0] and keyword[int((i + 1)/keyword_len)][(i+1)%keyword_len + 1] == encoder[j][1]:
                plainText.append(chr(j + ord("a")))

    print(*plainText)