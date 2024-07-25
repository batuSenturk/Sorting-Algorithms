def merge_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr)

    if end - start > 1:
        mid = (start + end) // 2
        yield from merge_sort(arr, start, mid)
        yield from merge_sort(arr, mid, end)

        left = arr[start:mid]
        right = arr[mid:end]

        i = j = 0
        k = start

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            yield arr, k
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            yield arr, k
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            yield arr, k
            k += 1

    yield arr, None
