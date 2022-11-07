def count_ones(num):
    return num.count('1')


def add_parity_bit(num):
    if count_ones(num) % 2 == 0:
        return num + '0'
    else:
        return num + '1'


def main():
    decimal = 702
    print("Decimal number:", decimal)
    binary = bin(decimal)
    print("Binary code:", binary)
    result_encoded = add_parity_bit(binary)
    print("Encoded (with parity bit):", result_encoded)

    print("------------------------------------")

    # error check: the number of ones without the parity bit should be odd if
    # it is 1, and even if it is 0
    if count_ones(result_encoded[-1]) % 2 == \
            count_ones(result_encoded[:-1]) % 2:
        parity_to_binary = result_encoded[:-1]
        print("Decoded - binary:", parity_to_binary)
        result_decoded = int(parity_to_binary, base=2)
        print("Decoded - decimal:", result_decoded)
    else:
        print("Error")


if __name__ == '__main__':
    main()
