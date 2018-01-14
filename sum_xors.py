import itertools

CONST = 10**9 + 7


def get_xor_sum(numbers: [int]):
    xor_results = {frozenset((num, )): num for num in numbers}
    sum_ = sum(numbers)
    for set_size in range(2, len(numbers) + 1):
        new_xor_results = {}
        for combination in itertools.combinations(numbers, set_size):
            new_result = xor_results[frozenset(combination[:-1])] ^ combination[-1]
            sum_ += new_result
            new_xor_results[frozenset(combination)] = new_result
        xor_results = new_xor_results

    return sum_


if __name__ == '__main__':
    print(get_xor_sum([47366630, 19757736, 38149628, 60702330, 26921049, 91387948, 76437713,]) % CONST)
