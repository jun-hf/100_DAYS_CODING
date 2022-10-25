"""
Given an array of positive numbers and a positive number 'k',
find the maximum sum of any contiguos subarray of size 'k'.

You need to use the end_window as the variable iterator, for your window.

"""    

def max_subarray(arr, k):
    sum_window, max_window = 0, 0
    start_window = 0

    for end_window in range(len(arr)):
        sum_window += arr[end_window]

        if end_window > k -2:
            max_window = max(sum_window, max_window)
            sum_window -= arr[start_window]
            start_window += 1
    
    return max_window

print(max_subarray([2, 1, 6, 8, 2, 3, 9, 9, 7], 2))