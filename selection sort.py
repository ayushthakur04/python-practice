#selection sort
def ss(arr, size):
    for i in range(size):
        min_ind = i
        for j in range(i + 1, size):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]

arr = [-1, 3, 0, 45, 6]
size = len(arr)
ss(arr, size)
print(arr)



[-1,0,3,6,45]
