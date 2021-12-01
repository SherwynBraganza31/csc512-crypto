#############################################################################
# A Simplified DES Program that encrypts in 4 rounds and uses 2 predetermined
# S boxes.
#
# Author: Sherwyn Braganza
#
# Date: 13 Nov 2021
#############################################################################
import barrel_shift
import random
#############################################################################
# Predetermined S-boxes
#############################################################################
S_box_1 = [[0b101, 0b010, 0b001, 0b110, 0b011, 0b100, 0b111, 0b000],
           [0b001, 0b100, 0b110, 0b010, 0b000, 0b111, 0b101, 0b011]]
S_box_2 = [[0b100, 0b000, 0b110, 0b101, 0b111, 0b001, 0b011, 0b010],
           [0b101, 0b011, 0b000, 0b111, 0b110, 0b010, 0b001, 0b100]]

#############################################################################
# Function: expander(number)
# Expands a 6 bit number into an 8bit number in the following way. The number
# corresponds to the bit position
#           1 2 3 4 5 6         ---> 6 bit original number
#         1 2 4 3 3 4 5 6       ---> 8 bit expansion
#
# params: number = The 6 bit number to expand
# returns: The 8 bit expansion of number
#
#############################################################################
def expander(number):
    return ((number & 0b110000) << 2) | ((number & 0b000100) << 3) \
           | ((number & 0b001000) << 1) | ((number & 0b000100) << 1) \
           | ((number & 0b001000) >> 1) | (number & 0b000011)

#############################################################################
# Function: baby_des_encrypt(plaintext, key, S_box_1, S_box_2, rounds)
# Performs an N round(N = value in rounds) encryption on the provided
# plaintext using the provided key and the two S-boxes. The encryption
# algorithm is a simple DES-like Feistel Algorithm described in the text
#
# params: plaintext - The plaintext to encrypt (a 12 bit number)
#         key       - A 9 bit number
#         S_box_1   - Predetermined S-box
#         S_box_2   - Predetermined S-box
#         rounds    - Number of encryption rounds to be performed
#
# returns: The 12 bit ciphertext.
#############################################################################
def baby_des_encrypt(plaintext, key, S_box_1, S_box_2, rounds):
    #key = key << 9 | key    # expand the key to and 18 bit number and take (offset + 9 bits)
    L = [0] * (rounds + 1)
    R = [0] * (rounds + 1)
    L[0] = plaintext >> 6   # left 6 bits of the plaintext
    R[0] = plaintext & 0b000000111111 # right 6 bits of the plaintext

    for i in range(0, rounds):
        L[i+1] = R[i]
        tempR = expander(R[i])  # expand R to get a 8 bit version of R
        key_i = ((barrel_shift._barrel_shift_left(key, i)) & 0b111111110) >> 1 # get 8 bits of Ki

        # follow the Feistel Algorithm
        tempR ^= key_i
        tempLR = (tempR >> 4)
        tempRR = (tempR & 0b00001111)

        # Compress R[i+1] using the S boxes
        R[i+1] = (S_box_1[int(tempLR >> 3)][int(tempLR & 0b0111)] << 3) | (S_box_2[int(tempRR >> 3)][int(tempRR & 0b0111)])
        R[i+1] = L[i] ^ R[i+1] # XOR R[i+1] with L[i] / final step of the algorithm

    return (L[rounds] << 6) | R[rounds]

#############################################################################
# Function: baby_des_decrypt(plaintext, key, S_box_1, S_box_2, rounds)
# Performs an N round(N = value in rounds) decryption on the provided
# ciphertext using the provided key and the two S-boxes. The decryption
# algorithm is the same as the encryption algorithm which is based on a
# simple DES-like Feistel Algorithm described in the text. The only difference
# is that L0 and R0 are swapped around.
#
# params: ciphertext- The cipher to decrypt (a 12 bit number)
#         key       - A 9 bit number
#         S_box_1   - Predetermined S-box
#         S_box_2   - Predetermined S-box
#         rounds    - Number of decryption rounds to be performed
#
# returns: The 12 bit plaintext.
#############################################################################
def baby_des_decrypt(ciphertext, key, S_box_1, S_box_2, rounds):
    #key = key << 9 | key
    L = [0] * (rounds + 1)
    R = [0] * (rounds + 1)
    R[0] = ciphertext >> 6
    L[0] = ciphertext & 0b000000111111

    for i in range(0, rounds):
        L[i+1] = R[i]
        tempR = expander(R[i])  # expand R to get a 8 bit version of R
        key_i = ((barrel_shift._barrel_shift_left(key, rounds - i - 1)) & 0b111111110) >> 1 # get 8 bits of Ki

        # follow the same Feistel Algorithm
        tempR ^= key_i
        tempLR = (tempR >> 4)
        tempRR = (tempR & 0b00001111)

        # Compress using the S boxes
        R[i+1] = (S_box_1[int(tempLR >> 3)][int(tempLR & 0b0111)] << 3) | (S_box_2[int(tempRR >> 3)][int(tempRR & 0b0111)])
        R[i+1] = L[i] ^ R[i+1]

    return (R[rounds] << 6) | L[rounds]


#############################################################################
# Intended way for this program to be used.
# Gives the user 2 modes
# a - Encryption mode where the user provides the key and the plaintext and th
#     program computes the ciphertext
# b - Decryption mode where the user provides the key and the ciphertext and the
#     program produces the plaintext
#############################################################################
def main():
    mode = 0
    print("Modes:\n" +
          "a: Encryption Mode - Provide keyword and the plaintext. The program will encrypt the plaintext and display it.\n" +
          "b: Decryption Mode - Provide ciphertext and keyword. The program will decrypt the ciphertext and display the plaintext.\n")

    mode = input("Your choice: ")
    mode = mode[0]

    if mode == "a":
        plaintext = int(input("Enter in a 12-bit binary string (no spaces): "), 2)
        key = int(input("Enter in 9-bit binary key: "), 2)

        #plaintext = 0b111010101111
        #key = 0b110100101

        #key = key << 9 | key
        cipherText = baby_des_encrypt(plaintext, key, S_box_1, S_box_2, 4)
        ## print ("The plaintext is: ", bin(baby_des_decrypt(cipherText, key, S_box_1, S_box_2, 4)))
        print ("The ciphertext is: ", bin(cipherText))

    elif mode == "b":
        cipherText = int(input("Enter in a 12-bit binary ciphertext string (no spaces): "), 2)
        key = int(input("Enter in 9-bit binary key: "), 2)

        plainText = baby_des_decrypt(cipherText, key, S_box_1, S_box_2, 4)
        print("The plaintext is: ", bin(plainText))


#############################################################################
# Quick and easy way to see that the program works.
# Generates plaintext and key pairs, encrypts that and then decrypts it to
# verify that the encryption and decryption mechanism works
#############################################################################
def test_cases():
    plaintext, key, ciphertext = [], [], []
    rounds = 4

    for i in range(0, 10):
        random_int = random.randint(0, 8191)
        while plaintext.count(random_int) > 0:
            random_int = random.randint(0, 8191)
        plaintext.append(random_int)

        random_int = random.randint(0, 511)
        while key.count(random_int) > 0:
            random_int = random.randint(0, 511)
        key.append(random_int)

        ciphertext.append(baby_des_encrypt(plaintext[i], key[i], S_box_1, S_box_2, rounds))
        print("The ciphertext for the plaintext ", bin(plaintext[i]), " and the key ", bin(key[i]), " is ", bin(ciphertext[i]))
        print("The decrypted plaintext for the same combo is ", bin(baby_des_decrypt(ciphertext[i], key[i], S_box_1, S_box_2, rounds)), end="\n\n")

if __name__ == "__main__":
    test_cases()




