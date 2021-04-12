from bubble_sort import bubble_sort

from plot import plot
arr = [10,8,6,4,2,1]

x =100
size = []
iters = []
for i in range(10):
    for j in range(len(arr)):
        arr[j] = len(arr) -j
    result, count = bubble_sort(arr)
    iters.append(count)
    size.append(len(arr))
    arr += arr

plot(size, iters)