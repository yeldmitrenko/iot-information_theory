# Helper function [ XOR - LOGIC ]
def xor(a, b):
    return '0' if (a == b) else '1'


# Helper function [ flipping bits ]
def flip(c):
    return '1' if (c == '0') else '0'


# BIN --> GRAY-CODE FUNC.
def binary2gray(binary):
    return bin(
        int(binary, base=2) ^ (int(binary, base=2) >> 1)
    )


# GRAY-CODE --> BIN FUNC.
def gray2binary(gray):
    binary = ""
    binary += gray[0]

    for i in range(1, len(gray)):

        if gray[i] == '0':
            binary += binary[i - 1]

        else:
            binary += flip(binary[i - 1])

    return binary


def main():
    decimal = "702"
    print("Decimal number:", decimal)
    binary_code = bin(int(decimal))
    print("Binary code:", binary_code)
    print("Gray code:", binary2gray(binary_code))

    print("--------------------")

    gray_code = "1111100001"
    print("Gray code:", gray_code)
    result = gray2binary(gray_code)
    print("Binary code:", result)
    decoded_decimal = int(result, base=2)
    print("Decimal number:", decoded_decimal)


if __name__ == '__main__':
    main()
