#https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true

def hourglassSum(arr):
    # Write your code here
    max_sum = -99
    for i in range(4):
        for j in range(4):
            s = 0
            for k in range(3):
                s += arr[i][j + k] + arr[i + 2][j + k]
            s += arr[i + 1][j + 1]
            print(s)
            max_sum = max(max_sum, s)
    return max_sum
