def kadanes_algorithm(arr):
    """
    This function implements the Kadane's algorithm to find the maximum sum of a contiguous subarray in a given array.

    Parameters:
    arr (list): A list of integers. The length of the list should be greater than or equal to 1.

    Returns:
    int: The maximum sum of a contiguous subarray in the given array.
    """
    max_current = max_global = arr[0]
    
    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > max_global:
            max_global = max_current
    
    return max_global
# Example usage
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
max_sum = kadanes_algorithm(arr)
print("Maximum sum of a contiguous subarray:", max_sum)


def dutch_national_flag_algorithm(arr, low, high):
    """
    This function implements the Dutch National Flag problem, also known as the 3-way partitioning problem.
    The problem is to sort an array of 0s, 1s, and 2s in one pass.

    Parameters:
    arr (list): A list of integers containing only 0s, 1s, and 2s. The length of the list should be greater than or equal to 1.
    low (int): The starting index of the range to be sorted.
    high (int): The ending index of the range to be sorted.

    Returns:
    list: The sorted array with 0s, 1s, and 2s in ascending order.
    """
    i = low
    mid = low
    high_end = high

    while mid <= high_end:
        if arr[mid] == 0:
            arr[i], arr[mid] = arr[mid], arr[i]
            i += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high_end] = arr[high_end], arr[mid]
            high_end -= 1

    return arr
# Example usage
arr = [1, 0, 2, 1, 0, 2, 1, 0]
sorted_arr = dutch_national_flag_algorithm(arr, 0, len(arr) - 1)
print("Sorted array:", sorted_arr)

#sliding window
def max_subarray_sum(arr, window_size):
    """
    This function calculates the maximum sum of a contiguous subarray of a given size in a given array.

    Parameters:
    arr (list): A list of integers. The length of the list should be greater than or equal to the window size.
    window_size (int): The size of the contiguous subarray. The value should be greater than 0 and less than or equal to the length of the array.

    Returns:
    int: The maximum sum of a contiguous subarray of the given size. If the window size is greater than the length of the array, None is returned.
    """
    if len(arr) < window_size:
        return None

    max_sum = sum(arr[:window_size])
    current_sum = max_sum

    for i in range(window_size, len(arr)):
        current_sum = current_sum - arr[i - window_size] + arr[i]
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage
arr = [1, -3, 2, 1, -1]
window_size = 3
max_sum = max_subarray_sum(arr, window_size)
print("Maximum sum of a contiguous subarray of size", window_size, ":", max_sum)