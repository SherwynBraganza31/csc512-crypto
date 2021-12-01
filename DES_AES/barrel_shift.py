def _barrel_shift_left(number, amount):
    number = int(number)
    amount = int(amount)%9
    return ((number << amount) & 511) | (number >> (9 - amount))

def _barrel_shift_right(number, amount):
    number = int(number)
    amount = int(amount)%9
    return (number >> amount) | ((number << (9 - amount)) & 511)

def main():
    print("Test cases:")

    number = [233, 123, 500, 352]
    amount = [1, 5, 27, 23246]

    for i in range(0, 4):
        for j in range(0, 4):
            print("The number ", bin(number[i]), " shifted right by ", amount[j], " is ", bin(_barrel_shift_right(number[i], amount[j])))
            print("The number ", bin(number[i]), " shifted left by ", amount[j], " is ",
                  bin(_barrel_shift_left(number[i], amount[j])), end="\n\n")

if __name__ == "__main__":
    main()