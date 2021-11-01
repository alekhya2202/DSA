"""
Given a 2D matrix of size NxN, print the sum of the elements of all its diagonals.

Input Format

First line of input contains T - number of test cases. First line of each test case contains N - size of the matrix. Each of the next N lines contains N integers - the elements of the matrix.

Constraints

1 <= T <= 100
1 <= N <= 100
-100 <= ar[i][j] <= 100

Output Format

For each test case, print the sum of the elements of all the diagonals, separated by newline. Refer samples for more clarity.

Sample Input
4
3
-5 0 4 
2 8 -6 
3 7 1 
1
-4 
2
5 -2 
-4 1 
6
-2 -3 -6 -5 50 3 
8 7 10 -5 -3 30 
6 3 70 9 -20 -7 
-9 9 -6 7 3 2 
-1 7 7 6 -4 3 
8 5 6 -9 40 8 

Sample Output
4 -6 4 9 3 
-4 
-2 6 -4 
3 80 -15 -29 22 86 51 13 4 4 8 

Explanation

Test Case 1
Sum of the elements of the 1st diagonal: 4
Sum of the elements of the 2nd diagonal: 0 + -6 = -6
Sum of the elements of the 3rd diagonal: -5 + 8 + 1 = 4
Sum of the elements of the 4th diagonal: 2 + 7 = 9
Sum of the elements of the 5th diagonal: 3

Test Case 2
Sum of the elements of the 1st and only diagonal: -4

Test Case 3
Sum of the elements of the 1st diagonal: -2
Sum of the elements of the 2nd diagonal: 5 + 1 = 6
Sum of the elements of the 3rd diagonal: -4
"""

tc = int(input())

for _ in range(tc):
    n = int(input())
    matrix = []
    for row in range(n):
        matrix.append(list(map(int, input().split())))
    #first half
    last = n - 1
    for gap in range(last, -1, -1):
        #print(gap)
        start = 0
        end = gap
        s = 0
        while(end <= last):
            s += matrix[start][end]
            start += 1
            end += 1
        print(s, end = " ")

    #second half
    last = n - 1
    diag = []
    for gap in range(1, n):
        #print(gap)
        start = gap
        end = 0
        s = 0
        while(start <= n - 1):
            s += matrix[start][end]
            start += 1
            end += 1
        print(s, end = " ")
