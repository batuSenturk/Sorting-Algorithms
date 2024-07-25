def flip(arr, k):
    start = 0
    while start < k:
        arr[start], arr[k] = arr[k], arr[start]
        start += 1
        k -= 1

def pancake_sort(arr):
    n = len(arr)
    for current_size in range(n, 1, -1):
        # Find the maximum element in the array from index 0 to current_size-1
        max_index = max(range(current_size), key=arr.__getitem__)

        # Move the maximum element to the end of the current array
        if max_index != current_size - 1:
            # Flip the maximum element to the front
            if max_index != 0:
                flip(arr, max_index)
                yield arr, max_index

            # Flip it to its correct position
            flip(arr, current_size - 1)
            yield arr, current_size - 1

    yield arr, None
