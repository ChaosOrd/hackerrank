

def get_all_multiples(max):
    sum_of_five_multiples = get_multiples(max, 5)
    sum_of_three_multiples = get_multiples(max, 3)
    sum_of_fifteen_multiples = get_multiples(max, 15)

    return sum_of_five_multiples + sum_of_three_multiples - sum_of_fifteen_multiples


def get_multiples(max, num):
    max = max - 1
    num_of_multiples = max // num
    sum_of_progression = (num_of_multiples + 1) * num_of_multiples // 2
    return num * sum_of_progression


if __name__ == '__main__':
    print(get_all_multiples(100))
