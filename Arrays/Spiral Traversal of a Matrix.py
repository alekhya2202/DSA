"""
Given a 2D square matrix, print the matrix in a spiral order. Refer examples for more details. From interviews point of view, after you scan the matrix in a 2D array, try to print the matrix in a spiral order without using any extra space.


Input Format

First line of input contains T - number of test cases. First line of each test case contains N - size of the matrix [NxN]. Its followed by N lines each containing N integers - elements of the matrix.

Constraints

1 <= T <= 100
1 <= N <= 100
-100 <= ar[i][j] <= 100

Output Format

For each test case, print the matrix in a spiral order, separated by newline.

Sample Input 0

4
1
1
2
1 2
4 3
3
1 2 3
8 9 4
7 6 5
5
-44 25 -52 69 -5 
17 22 51 27 -44 
-79 28 -78 1 -47 
65 -77 -14 -21 -6 
-96 43 -21 -20 90 

Sample Output 0

1 
1 2 3 4 
1 2 3 4 5 6 7 8 9 
-44 25 -52 69 -5 -44 -47 -6 90 -20 -21 43 -96 65 -79 17 22 51 27 1 -21 -14 -77 28 -78 

Explanation 0

Self Explanatory
"""
#reference - https://youtu.be/TmweBVEL0I0

def matrix_spiral():
    n = int(input())
    matrix = []
    for row in range(n):
        matrix.append(list(map(int, input().split())))
    curr_row, curr_col = 0, 0
    last_row, last_col = n - 1, n - 1

    while(curr_col <= last_col and curr_row <= last_row):
        for i in range(curr_col, last_col + 1):
            print(matrix[curr_row][i], end = " ")

        curr_row += 1

        for j in range(curr_row, last_row + 1):
            print(matrix[j][last_col], end = " ")
        last_col -= 1

        if(curr_row <= last_row):
            for i in range(last_col, curr_col - 1, -1):
                print(matrix[last_row][i], end = " ")
            last_row -= 1

        if curr_col <= last_col:
            for i in range(last_row, curr_row - 1, -1):
                print(matrix[i][curr_col], end = " ")
            curr_col += 1

tc = int(input())
for _ in range(tc):
    matrix_spiral()
    print()
