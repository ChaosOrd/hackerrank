#!/bin/python3

import sys


def equal(arr):
    num_of_actions = 0
    min_num = min(arr)
    for colleague_num in range(len(arr)):
        variants = []
        diff = arr[colleague_num] - min_num
        variants.append(num_of_ops_to_zero(diff))
        variants.append(num_of_ops_to_zero(diff + 1) + 1)
        variants.append(num_of_ops_to_zero(diff + 2) + 1)
        variants.append(num_of_ops_to_zero(diff + 3) + 2)
        variants.append(num_of_ops_to_zero(diff + 4) + 2)
        num_of_actions += min(variants)

    return num_of_actions


def num_of_ops_to_zero(num):
    num_left = num
    num_5 = num_left // 5
    num_left = num_left % 5
    num_2 = num_left // 2
    num_left = num_left % 2
    num_1 = num_left
    return num_5 + num_2 + num_1


if __name__ == '__main__':
    print(equal([1, 5, 5]))
