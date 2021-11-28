"""
Problem Description

Given an one-dimensional unsorted array A containing N integers.

You are also given an integer B, find if there exists a pair of elements in the array whose difference is B.

Return 1 if any such pair exists else return 0.



Problem Constraints
1 <= N <= 105
-103 <= A[i] <= 103
-105 <= B <= 105


Input Format
First argument is an integer array A of size N.

Second argument is an integer B.



Output Format
Return 1 if any such pair exists else return 0.

"""
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        p1 = 0
        p2 = 1

        while(p1 < len(A) and p2 < len(A)):
            if p1 != p2 and A[p2] - A[p1] == B:
                return 1

            elif A[p2] - A[p1] < B:
                p2 += 1

            else:
                p1 += 1

        return 0
