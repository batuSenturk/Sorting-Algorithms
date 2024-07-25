def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pi_gen = partition(arr, low, high)
        while True:
            try:
                arr, pi = next(pi_gen)
                yield arr, pi
            except StopIteration as e:
                pi = e.value
                break

        yield from quick_sort(arr, low, pi - 1)
        yield from quick_sort(arr, pi + 1, high)

    yield arr, None

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            yield arr, j
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    yield arr, i + 1
    return i + 1
