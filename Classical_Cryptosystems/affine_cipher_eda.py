#############################################################################
# Program that encrypts or decrypts a cipher according to the rules of
# affine ciphers.
# It has 2 modes:-
# a: Encryption Mode - Encrypts the given plaintext with the α and β values
#					   provided
# b: Decryption Mode - Decrypts the given ciphertext and diplays the
#					   plaintext
# c: Attack Mode	 - Decrypts the given ciphertext by doing a freq
#					   analysis to find the key.
#
# Author: Sherwyn Braganza
#
# Date: 12 Sep 2021
#
#############################################################################


import math
import numpy as np
from freq_calc import get_freq

mode = 0
print("Modes:\n" + 
	"a: Encryption Mode - Provide α and β values and the plaintext. The program will encrypt the plaintext and display it.\n" +
	"b: Decryption Mode - Provide ciphertext and key. The program will decrypt the ciphertext and display the plaintext.\n" +
	"c: Attack Mode - Provide ciphertext. The program will get the key, decrypt the ciphertext and display the plaintext.\n")

mode = input("Your choice: ")
print()
mode = mode[0]

####################### Encryption Mode #######################
if mode == "a":
	# get inputs
	alpha = int(input("Enter in α:"))
	beta  = int(input("Enter in β:"))
	plainText = input("Enter in plaintext:")

	plainText = plainText.lower()
	plainText = list(str(plainText))

	# loop to eliminate all spaces in the plaintext
	while True:
			try:
				plainText.remove(" ")
			except ValueError:
				break

	# the plaintext to cipher text conversion function
	# based on ciphertext[i] = plaintext[i] * alpha + beta
	# overwrites the same plaintext container for optimization reasons
	for i in range(0, len(plainText)):
		if plainText[i].isalpha():
			plainText[i] = chr(((ord(plainText[i]) - ord('a')) * alpha + beta)%26 + ord('a'))
	
	print(*plainText)


#################### Decryption Mode #########################
elif mode == "b":

	alpha = int(input("Enter in α:"))
	beta  = int(input("Enter in β:"))
	cipherText = input("Enter in CipherText:")

	cipherText = list(str(cipherText))

	# loop to eliminate all spaces in the plaintext
	while True:
		try:
			cipherText.remove(" ")
		except ValueError:
			break

	## decrypt ciphertext using the alpha and beta values.
	for i in range(0, len(cipherText)):
		cipherText[i] = (chr((((ord(cipherText[i]) - 97) - beta) * pow(alpha, -1, 26)) % 26 + 97))

	print(*cipherText)

##################### Attack Mode #########################
else:
	cipherText = input("Enter in the ciphertext that is atleast 130 chars long:")
	freq_hash_map = get_freq(cipherText)
	cipherText = list(str(cipherText))

	# loop to eliminate all spaces in the plaintext
	while True:
		try:
			cipherText.remove(" ")
		except ValueError:
			break

	## This part finds the alpha and beta values (the key) and then uses it to decrypt the ciphertext
	## TO - DO : replace with own modinv function
	alpha = (freq_hash_map[0][0] - freq_hash_map[1][0]) * pow(4-19, -1, 26) % 26
	beta = (freq_hash_map[0][0] - alpha * 4) %26

	## decrypt ciphertext using the calculated alpha and beta values.
	for i in range(0, len(cipherText)):
		cipherText[i] = (chr((((ord(cipherText[i]) - 97) - beta) * pow(alpha, -1, 26)) % 26 + 97))

	print(*cipherText)




		
