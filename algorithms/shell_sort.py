def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    # Start with a big gap, then reduce the gap
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Shift earlier gap-sorted elements up until the correct location for arr[i] is found
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                yield arr, j
            # Put temp (the original arr[i]) in its correct location
            arr[j] = temp
            yield arr, i
        gap //= 2

    yield arr, None
