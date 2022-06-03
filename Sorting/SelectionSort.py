#selection sort

def selectionsort(arr):
    for i in range(len(arr)):
        min_el = arr[i]
        idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < min_el:
                min_el = arr[j]
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]
    return arr

#print(selectionsort([1,6,3,44,76,90,33]))

arr = list(map(int, input().split()))
print(selectionsort(arr))
