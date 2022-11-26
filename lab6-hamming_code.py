import numpy as np
from functools import reduce
import operator as op


def generate_powers_of_two(b_num):
    p_val = 1
    i = 0
    result = []
    while p_val < len(b_num):
        result.append(2 ** i)
        i += 1
        p_val = 2 ** i
    return result


def convert_to_hamming(b_num):
    powers_of_two = generate_powers_of_two(b_num)
    arr_number_of_ones = []
    b_num = [digit for digit in b_num]
    for i in powers_of_two:
        b_num.insert(i - 1, '2')

    for i in range(len(powers_of_two)):
        j = 1
        number_of_ones = 0
        while j <= len(b_num):
            if j in powers_of_two:
                j += 1
                continue
            b = format(j, '04b')
            if int(b[-(i + 1)]) == 1 and int(b_num[j - 1]) == 1:
                number_of_ones += 1
            j += 1
        arr_number_of_ones.append(number_of_ones)
    j = 0
    for i in range(len(b_num)):
        if b_num[i] == '2':
            if arr_number_of_ones[j] % 2:
                b_num[i] = '1'
            else:
                b_num[i] = '0'
            j += 1
    return np.array([int(digit) for digit in b_num])


def decode_hamming(hamming):
    pos = reduce(op.xor, [i for i, bit in enumerate(hamming, 1) if bit])
    if pos:
        print("Error position:", pos)
        hamming_print = nparray_to_str(hamming)
        print("Before correction:", hamming_print)
        hamming[pos - 1] = int(not hamming[pos - 1])
        hamming_print = nparray_to_str(hamming)
        print("After correction:", hamming_print)
    else:
        print("Error is not found")

    powers_of_two = generate_powers_of_two(hamming)
    powers_of_two = [i - 1 for i in powers_of_two]
    hamming = np.delete(hamming, powers_of_two)
    return nparray_to_str(hamming)


def nparray_to_str(arr):
    res = ''
    for digit in arr:
        res += str(digit)
    return res


if __name__ == '__main__':
    print("Enter decimal number:")
    binary_num = bin(int(input()))
    print("Binary number:", binary_num[2:])
    hamming_code = convert_to_hamming(binary_num[2:])
    ham_code = nparray_to_str(hamming_code)
    print("Hamming code:", ham_code)
    back_to_bin = decode_hamming(hamming_code)
    print("Decoded Hamming code:", back_to_bin)
    print("\nDecoded decimal number:", int(back_to_bin, 2))

    print("\n------------------------------------------")
    hamming_code = np.array([1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1])
    ham_code = nparray_to_str(hamming_code)
    print(ham_code)
    print(decode_hamming(hamming_code))
