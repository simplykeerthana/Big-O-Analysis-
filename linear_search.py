def linear_search(arr, x, count = 0):
    for i in range(len(arr)):
        count +=1
        if arr[i] ==x:
            return -1, count
    return -1, count
