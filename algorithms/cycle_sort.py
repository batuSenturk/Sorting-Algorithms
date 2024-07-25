def cycle_sort(arr):
    writes = 0

    for cycle_start in range(0, len(arr) - 1):
        item = arr[cycle_start]

        # Find where to place the item
        pos = cycle_start
        for i in range(cycle_start + 1, len(arr)):
            if arr[i] < item:
                pos += 1

        # If the item is already in the correct position
        if pos == cycle_start:
            continue

        # Otherwise, place the item to its correct position
        while item == arr[pos]:
            pos += 1
        arr[pos], item = item, arr[pos]
        writes += 1
        yield arr, pos

        # Rotate the rest of the cycle
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, len(arr)):
                if arr[i] < item:
                    pos += 1
            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]
            writes += 1
            yield arr, pos

    yield arr, None
