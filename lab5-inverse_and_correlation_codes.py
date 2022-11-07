def inverse_binary(num):
    result = ''
    for i in num:
        if i == '1':
            result += '0'
        else:
            result += '1'
    return result


def encode_inverse(num):
    if num.count('1') % 2 == 0:
        num *= 2
    else:
        num += inverse_binary(num)
    return num


def xor(x, y):
    x = False if x == '0' else True
    y = False if y == '0' else True
    return False if x == y else x or y


def decode_inverse(combination):
    first_info_half = combination[:len(combination) // 2]
    second_verification_half = combination[len(combination) // 2:]

    print("----------------------------------------")
    print("Info first code part:", first_info_half)
    print("Verification second code part:", second_verification_half)
    print("----------------------------------------")

    valid_result = ''
    if first_info_half.count('1') % 2 == 0:
        if first_info_half == second_verification_half:
            valid_result = second_verification_half
        else:
            print("Verification part is different from info part")
            return False
    else:
        valid_result += inverse_binary(second_verification_half)
        if first_info_half != valid_result:
            print("Verification part after enversion is different from info part")
            return False

    print(first_info_half + "\n    ⊕\n" + second_verification_half + "\n----------")

    for i in range(0, len(first_info_half)):
        result = xor(first_info_half[1], valid_result[i])
        if result:
            return first_info_half
        else:
            print("Found an error, the sum is not null")
            return False


def encode_correlation(num):
    encoded_cor = ''
    for i in num:
        encoded_cor += i + inverse_binary(i)
    return encoded_cor


def decode_correlation(num):
    pairs = []
    for i in range(0, len(num) - 1, 2):
        pairs.append([num[i], num[i + 1]])

    print("-----------------\nSplitting combinations into pairs:", pairs)
    for i in range(0, len(pairs)):
        print(pairs[i][0], "⊕", pairs[i][1], "=", int(int(pairs[i][0]) != int(pairs[i][1])))

    if check_validation(pairs):
        decoded_result = ""
        for elem in pairs:
            decoded_result += elem[0]
        return decoded_result
    else:
        print("Found an error, the sum is not null")
        return False


def check_validation(pairs):
    pairs_sums = [xor(pairs[i][0], pairs[i][1]) for i in range(0, len(pairs))]
    return False not in pairs_sums


def main():
    decimal = 702
    print("Decimal number:", decimal)

    print("                     Inverse code\n")
    binary_code = bin(decimal)
    print("Binary code:", binary_code)
    inverse_number = encode_inverse(binary_code[2:])
    print("Encoded inverse:", inverse_number)
    decoded_num = decode_inverse(inverse_number)
    print("Decoded inverse:", decoded_num)
    print("Decoded decimal number:", int(decoded_num, 2))

    print("\n#############################################\n")
    print("                     Correlation code\n")
    correlation_code = encode_correlation(binary_code[2:])
    print("Binary code:", binary_code)
    print("Encoded correlation code:", correlation_code)
    decoded_correlation_code = decode_correlation(correlation_code)
    print("Decoded correlation number:", decoded_correlation_code)
    print("Decoded decimal number:", int(decoded_correlation_code, 2))


if __name__ == '__main__':
    main()
