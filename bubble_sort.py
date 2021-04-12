def bubble_sort(arr, count =0):
    for i in range(len(arr)):
        count += 1
        for j in range(len(arr) -1):
            count +=1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr, count