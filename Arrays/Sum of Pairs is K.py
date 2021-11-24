"""Given an array of integers and a number K, check if there exist a pair of indices i,j s.t. a[i] + a[j] = K and i!=j.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines, first line of each test case contains N - size of the array and K, and the next line contains N integers - the elements of the array.

Constraints

30 points
1 <= T <= 100
2 <= N <= 1000

70 points
1 <= T <= 300
2 <= N <= 10000

General Constraints
-108 <= K <= 108
-108 <= ar[i] <= 108

Output Format

For each test case, print "True" if such a pair exists, "False" otherwise, separated by newline."""

#Two pointer approach
def findPair(arr, N, K):
    p1 = 0
    p2 = N - 1
    while(1):
        if arr[p1] + arr[p2] == K:
            return "True"
        elif arr[p1] + arr[p2] > K:
            p2 -= 1
        else:
            p1 += 1
        if p1 == p2:
            break
    return "False"

tc = int(input())
for _ in range(tc):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    print(findPair(arr, N, K))
