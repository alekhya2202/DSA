def BSort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

print(BSort([1,5,3,7,93,45,65]))
print(BSort([45,89,23,74,90]))
