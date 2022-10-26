"""
Given an array of positive nuymbers and a positive number S, find the lenght
of the smallest contigous subarray whose sum is greater than or equal to S. Return 0, if
no such subarray exist.

[2, 4, 5, 3, 1, 8, 9] k = 10
                |
                   |
"""
import math

def algo(arr, k):
    min_len = math.inf
    wind_start = 0
    wind_sum = 0

    for wind_end in range(len(arr)):
        wind_sum += arr[wind_end]

        while wind_sum >= k:
            min_len = min(min_len, wind_end - wind_start + 1)
            wind_sum -= arr[wind_start]
            wind_start += 1

    if min_len == math.inf:
        return 0

    return min_len

print(algo([2, 4, 5, 3, 1, 8, 9], 10))


