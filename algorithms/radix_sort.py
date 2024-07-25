def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Store count of occurrences in count[]
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
        yield arr, i

    # Change count[i] so that count[i] contains the actual
    # position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]
        yield arr, i

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        yield output, i
        i -= 1

    # Copy the output array to arr[], so that arr now
    # contains sorted numbers according to the current digit
    for i in range(n):
        arr[i] = output[i]
        yield arr, i

def radix_sort(arr):
    # Find the maximum number to know the number of digits
    max_val = max(arr)

    # Do counting sort for every digit. Note that instead of passing the digit number,
    # exp is passed. exp is 10^i where i is the current digit number
    exp = 1
    while max_val // exp > 0:
        yield from counting_sort_for_radix(arr, exp)
        exp *= 10

    yield arr, None
