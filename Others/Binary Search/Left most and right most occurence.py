def lmost(arr, num):
    lo = 0
    hi = len(arr) - 1
    ans = -1

    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == num:
            ans = mid
            hi = mid - 1
            
        elif arr[mid] > num:
            hi = mid -1

        else:
            lo = mid + 1

    return ans

def rmost(arr, num):
    lo = 0
    hi = len(arr) - 1
    ans = -1

    while(lo <= hi):
        mid = (lo + hi) // 2
        if arr[mid] == num:
            ans = mid
            lo = mid + 1

        elif arr[mid] > num:
            hi = mid - 1
        else:
            lo = mid + 1
    return ans


arr = [3,9,9,45,75,75,75,432]
#lmost(7) = 5
#rmost(7) = 10
print(lmost(arr, 3))
print(lmost(arr, 75))
print(rmost(arr, 3))
print(rmost(arr, 75))
