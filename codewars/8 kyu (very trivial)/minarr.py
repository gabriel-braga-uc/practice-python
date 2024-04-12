def find_smallest_int(arr):
    arr_min = arr[0]
    for x in arr:
        if x < arr_min:
            arr_min = x
    return arr_min