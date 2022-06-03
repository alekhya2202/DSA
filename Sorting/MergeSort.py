#Merge Sort

def Merge(arr, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid 

    a1 = [0] * n1
    a2 = [0] * n2

    for i in range(n1):
        a1[i] = arr[low + i]

    for j in range(n2):
        a2[j] = arr[mid + 1 + j]
        
    i = 0
    j = 0
    k = low

    while(i < n1 and j < n2):
        if(a1[i] < a2[j]):
            arr[k] = a1[i]
            i += 1

        else:
            arr[k] = a2[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = a1[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = a2[j]
        j += 1
        k += 1

def MS(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        MS(arr, low, mid)
        MS(arr, mid + 1, high)
        Merge(arr, low, mid, high)


arr = list(map(int, input().split()))
lo = 0
hi = len(arr) - 1
MS(arr, lo, hi)
print(arr)
