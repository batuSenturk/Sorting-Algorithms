def odd_even_sort(arr):
    n = len(arr)
    sorted = False

    while not sorted:
        sorted = True
        # Perform Bubble sort on odd indexed element
        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False
                yield arr, i
        # Perform Bubble sort on even indexed element
        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False
                yield arr, i

    yield arr, None
