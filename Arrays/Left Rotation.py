#Problem stat
#https://www.hackerrank.com/challenges/array-left-rotation/problem?isFullScreen=true

def rotateLeft(d, arr):
    # Write your code here
    arr_len = len(arr)
    rotated = []
    if d % arr_len == 0:
        return arr
    d = d % arr_len
    rotated = [*arr[d:], *arr[0: d]]
    #print(rotated)
    return rotated
