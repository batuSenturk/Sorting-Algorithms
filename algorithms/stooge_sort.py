def stooge_sort(arr, l=0, h=None):
    if h is None:
        h = len(arr) - 1
    if l >= h:
        return

    if arr[l] > arr[h]:
        arr[l], arr[h] = arr[h], arr[l]
        yield arr, h

    if h - l + 1 > 2:
        t = (h - l + 1) // 3
        yield from stooge_sort(arr, l, h - t)
        yield from stooge_sort(arr, l + t, h)
        yield from stooge_sort(arr, l, h - t)
