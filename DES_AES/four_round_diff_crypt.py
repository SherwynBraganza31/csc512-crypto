from baby_des_ed import baby_des_encrypt, S_box_1, S_box_2, expander
from barrel_shift import _barrel_shift_right, _barrel_shift_left
import random

_SAMPLE_SIZE = 10
_ROUNDS = 4

def four_round_diff_crypt(hidden_key, rounds):
    hidden_key = int(hidden_key)

    L0 = []
    for i in range(0, _SAMPLE_SIZE):
        random_int = random.randint(1, 15)
        while L0.count(random_int) > 0:
            random_int = random.randint(1, 15)
        L0.append(random_int)

    L0_star = []
    R0 = [0b011011] * _SAMPLE_SIZE

    L4, R4, L4_star, R4_star = [], [], [], []

    for i in range(0, _SAMPLE_SIZE):
        # Encrypt L1 and R1 in 'r' rounds and store L4 and R4
        temp = baby_des_encrypt((L1[i] << 6) | (R1[i]), _barrel_shift_left(hidden_key, 1), S_box_1, S_box_2, rounds)
        L4.append(temp >> 6)
        R4.append(temp & 0b000000111111)

        # Encrypt L1_star and R1_star(same as R1) in 'r' rounds and store L4 and R4
        temp = baby_des_encrypt((L1_star[i] << 6) | (R1[i]), _barrel_shift_left(hidden_key, 1), S_box_1, S_box_2,
                                rounds)
        L4_star.append(temp >> 6)
        R4_star.append(temp & 0b000000111111)

    #############################################################################
    # From mathematically working out Differential Cryptanalysis, we end up with an this equation
    # Rn' ^ L1' = f(Ln, Kn) ^ f(Ln_star, Kn)
    #
    # The net step attempts to calculate Rn' ^ L1' and store it as a target to be achieved.
    # More intuitively the target_LHS is what the XOR of the S-box outputs should evaluate.
    #############################################################################
    target_LHS = []
    for i in range(0, _SAMPLE_SIZE):
        target_LHS.append((R4[i] ^ R4_star[i]) ^ (L1[i] ^ L1_star[i]))

    #############################################################################
    # The next step involves reverse engineering the S-boxes and finding the
    # input pairs that give us the desired output pairs in target_LHS
    #
    # They are stored as a list of a list of 2-tuples
    #############################################################################
    input_pairs_S1 = []
    input_pairs_S2 = []
    for i in range(0, _SAMPLE_SIZE):
        input_pairs_S1.append([])
        input_pairs_S2.append([])
        for j in range(0, 16):
            for k in range(0, 16):
                if (S_box_1[int(j / 8)][j % 8] ^ S_box_1[int(k / 8)][k % 8]) == (target_LHS[i] >> 3):
                    input_pairs_S1[i].append((j, k))
                if (S_box_2[int(j / 8)][j % 8] ^ S_box_2[int(k / 8)][k % 8]) == (target_LHS[i] & 7):
                    input_pairs_S2[i].append((j, k))

    #############################################################################
    # Reduce the input pairs by checking to see which solve for the same value of
    # K and discarding those that don't
    #
    # Mathematically, for each input pair (x, y), computing Kn
    # Kn = x ^ Ln and  Kn = y ^ Ln_star should return the same value of Kn
    #############################################################################
    for i in range(0, _SAMPLE_SIZE):
        # FOR input pairs from S_box_1
        j = 0
        while j < (len(input_pairs_S1[i])):
            temp1, temp2 = input_pairs_S1[i][j]
            if (temp1 ^ temp2) != (expander(L4[i] ^ L4_star[i]) >> 4) or (
                    temp1 ^ (expander(L4[i]) >> 4) != temp2 ^ (expander(L4_star[i]) >> 4)):
                input_pairs_S1[i].remove((temp1, temp2))
            else:
                j = j + 1

        # FOR input pairs from S_box_2
        j = 0
        while j < (len(input_pairs_S2[i])):
            temp1, temp2 = input_pairs_S2[i][j]
            if (temp1 ^ temp2) != (expander(L4[i] ^ L4_star[i]) & 15) or (
                    temp1 ^ (expander(L4[i]) & 15) != temp2 ^ (expander(L4_star[i]) & 15)):
                input_pairs_S2[i].remove((temp1, temp2))
            else:
                j = j + 1

    #############################################################################
    # Generating a dictionary with keys 0 - 15, to count frequencies of Kn occurrences
    # Based on the principle of 4 round differential cryptanalysis, where if a
    # probable key is the right key it should occur most frequently.
    #############################################################################
    lower_key_freq = {0: 0}
    upper_key_freq = {0: 0}
    for i in range(1, 16):
        lower_key_freq.update({i: 0})
        upper_key_freq.update({i: 0})

    # count the frequencies of the occurrences of the lower and upper 4 bits of the round key
    for i in range(0, _SAMPLE_SIZE):
        L = expander(L4[i])
        lower_L = L & 15
        upper_L = L >> 4
        for j in range(0, len(input_pairs_S1[i])):
            upper_key_freq[input_pairs_S1[i][j][0] ^ upper_L] = upper_key_freq.get(
                input_pairs_S1[i][j][0] ^ upper_L) + 1
        for j in range(0, len(input_pairs_S2[i])):
            lower_key_freq[input_pairs_S2[i][j][0] ^ lower_L] = lower_key_freq.get(
                input_pairs_S2[i][j][0] ^ lower_L) + 1

    # #############################################################################
    # # Find the most occurring lower and upper 4 bit permutation and store that
    # # as the guessed key
    # #############################################################################
    # L_key = 0
    # U_key = 0
    # for i in range(1, 16):
    #     if (lower_key_freq.get(i) > lower_key_freq.get(L_key)):
    #         L_key = i
    #     if (upper_key_freq.get(i) > upper_key_freq.get(U_key)):
    #         U_key = i
    #
    # #############################################################################
    # # combine the possible key in the form UUUULLLL* where U
    # #############################################################################
    # possible_key = _barrel_shift_right((U_key << 5) | (L_key << 1) | 1, rounds)
    #
    # test1 = baby_des_encrypt((L1[0] << 6) | (R1[0]), _barrel_shift_left(possible_key, 1), S_box_1, S_box_2, rounds)
    # test2 = baby_des_encrypt((L1[1] << 6) | (R1[1]), _barrel_shift_left(possible_key, 1), S_box_1, S_box_2, rounds)
    # if test1 != ((L4[0] << 6) | R4[0]) and test2 != ((L4[1] << 6) | R4[1]):  # and baby_des_encrypt((L1[1] << 6) | (R1[1]), possible_key, S_box_1, S_box_2, 3) == ((L4[1] << 3) | R4[1]):
    #     possible_key = possible_key ^ 0b001000000

    return lower_key_freq, upper_key_freq


def test_cases():
    rand_key = random.randint(1, 511)
    lower_key_freq, upper_key_freq = four_round_diff_crypt(rand_key, _ROUNDS)

    for i in range(0, 12):
        temp_lower_key_freq, temp_upper_key_freq = four_round_diff_crypt(rand_key, _ROUNDS)
        for j in range(0, 16):
            lower_key_freq[i] = lower_key_freq.get(i) + temp_lower_key_freq.get(i)
            upper_key_freq[i] = upper_key_freq.get(i) + temp_upper_key_freq.get(i)

    #############################################################################
    # Find the most occurring lower and upper 4 bit permutation and store that
    # as the guessed key
    #############################################################################
    L_key = 0
    U_key = 0
    for i in range(1, 8):
        if (lower_key_freq.get(i) > lower_key_freq.get(L_key)):
            L_key = i
        if (upper_key_freq.get(i) > upper_key_freq.get(U_key)):
            U_key = i

    #############################################################################
    # combine the possible key in the form UUUULLLL* where U
    #############################################################################
    possible_key = _barrel_shift_right((U_key << 5) | (L_key << 1) | 1, _ROUNDS)

    L1 = 0b000111
    R1 = 0b011011
    test1 = baby_des_encrypt((L1 << 6) | (R1), _barrel_shift_left(rand_key, 1), S_box_1, S_box_2, _ROUNDS)
    test2 = baby_des_encrypt((L1 << 6) | (R1), _barrel_shift_left(possible_key, 1), S_box_1, S_box_2, _ROUNDS)
    if test1 != test2: # and baby_des_encrypt((L1[1] << 6) | (R1[1]), possible_key, S_box_1, S_box_2, 3) == ((L4[1] << 3) | R4[1]):
        possible_key = possible_key ^ 0b001000000

    print("A hidden key ", bin(rand_key), " was generated. The program guessed the key to be ", \
          bin(possible_key), "and the XOR of the two keys is", bin(rand_key ^ possible_key),  end="\n")


if __name__ == "__main__":
    test_cases()