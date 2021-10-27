#############################################################################
# Program that calculates the letter frequency of a given text.
# Base Program for other attack based programs in this project.
#
# Can be run as a standalone program but main use is to use the get_freq
# helper function to get the frequencies of all letters in the text.
# Author: Sherwyn Braganza
#
# Date: 25 Oct 2021
#############################################################################
from operator import itemgetter

#############################################################################
# get_freq
#
# params - plainText = The plaintext on which a frequency search must be
#                      performed.
#
# returns freq_hash_map = A 2-D array like hash map containing an alphabet
#                         with its corresponding frequency.
#
#############################################################################
def get_freq(plainText):
    # make sure that the entire string is in lowercase
    plainText = plainText.lower()
    plainText = list(str(plainText))

    # create a 2-D matrix like Hash Map where the first element is the alphanumeric
    # value of itself and the second is the frequency of that alphabet.
    freq_hash_map = [[0, 0]]
    for i in range(1, 26):
        freq_hash_map.append([i, 0])

    # eliminate all empty spaces in the key or plaintext
    while True:
        try:
            plainText.remove(" ")
        except ValueError:
            break

    for i in range(0, len(plainText)):
        if plainText[i].isalpha():
            # calculate the hash_index or key to the hash map
            hash_index = ord(plainText[i]) - ord('a')
            # increment value of the hashed variable by 1
            freq_hash_map[hash_index][1] = freq_hash_map[hash_index][1] + 1

    # sort hash map to in descending order of element frequencies.s
    freq_hash_map = sorted(freq_hash_map, key=itemgetter(1), reverse=True)
    return freq_hash_map


######################### Standalone Program Part #############################

#
#plainText = input("Enter in a text that is sufficiently long (around 30 words): ")
#hash_map = get_freq(plainText)
#print("\n")
#
#for j in range(0, 6):
#    print(chr(hash_map[j][0] + ord('a')), " = ", round(hash_map[j][1]/len(plainText), 4), "\n")
#
