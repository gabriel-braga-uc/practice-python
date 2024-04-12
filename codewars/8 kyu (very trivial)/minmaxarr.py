def minimum(arr):
    arr_min = arr[0]
    for x in arr:
        if x < arr_min:
            arr_min = x
    return arr_min

def maximum(arr):
    arr_max = arr[0]
    for x in arr:
        if x > arr_max:
            arr_max = x
    return arr_max