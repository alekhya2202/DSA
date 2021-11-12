"""
A robot is located at the top-left corner of a m x n grid.

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0 for x in range(n)] for x in range(m)]
        if m == 1 and n == 1:
            return 1
        elif m == 0 or n == 0:
            return 0
        if memo[m - 1][n - 1] != 0:
            return memo[m - 1][n - 1]
        memo[m - 1][n - 1] = Solution.uniquePaths(self, m - 1, n) + Solution.uniquePaths(self, m, n - 1)
        return memo[m - 1][n - 1]

#run time error when submitted on leetcode! Yet to optimise
