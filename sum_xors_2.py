CONST = 10 ** 9 + 7


def get_xor_sum(numbers: [int]):
    result = 0
    for number in numbers:
        result |= number

    return result * (2 ** (len(numbers) - 1)) % CONST


if __name__ == '__main__':
    print(get_xor_sum([1, 2, 3]) % CONST)
