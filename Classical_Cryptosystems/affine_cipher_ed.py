#############################################################################
# Program that encrypts or decrypts a cipher according to the rules of 
# affine ciphers.
# It has 2 modes:-
# a: Encryption Mode - Encrypts the given plaintext with the α and β values
#					   provided
# b: Decryption Mode - Decrypts the given ciphertext and diplays the
#					   plaintext
#
# Author: Sherwyn Braganza
#
# Date: 12 Sep 2021
#
#############################################################################


import math
import numpy as np

mode = 0
print("Modes:\n" + 
	"a: Encryption Mode - Provide α and β values and the plaintext. The program will encrypt the plaintext and display it.\n" +
	"b: Decryption Mode - Provide ciphertext. The program will decrypt the ciphertext and display the plaintext.\n")

mode = input("Your choice: ")
print()
mode = mode[0]

if mode == "a":
	alpha = int(input("Enter in α:"))
	beta  = int(input("Enter in β:"))
	plainText = input("Enter in plaintext:")

	plainText = list(str(plainText))

	while True:
			try:
				plainText.remove(" ")
			except ValueError:
				break

	for i in range(0, len(plainText)):
		plainText[i] = chr(((ord(plainText[i]) - ord('a')) * alpha + beta)%26 + ord('a'))
	
	print(*plainText)

else:
	cipherText = list(str(input("Enter in the ciphertext:")))
	plainText = list(str(input("Enter first two letters of the plaintext:")))

	## TO - DO : replace with own modinv function
	alpha = (ord(cipherText[0]) - ord(cipherText[1])) * pow(int(ord(plainText[0]) - ord(plainText[1])), -1, 26)
	beta = ord(cipherText[0]) - 97 - alpha*(ord(plainText[0]) - 97)

	for i in range(2, len(cipherText)):
		plainText.append(chr((((ord(cipherText[i]) - 97) - beta) * pow(alpha, -1, 26)) % 26 + 97))

	print(*plainText)




		
