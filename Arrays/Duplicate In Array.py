"""
Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than O(n) 
space and traversing the stream sequentially O(1) times.

Source:
question - https://www.interviewbit.com/problems/find-duplicate-in-array/
reference - https://www.youtube.com/watch?v=lf2w3C82jYA
"""

class Solution:
    def repeatedNumber(self, A):
        A = list(A)
        for ele in A:
            number = ele
            if(ele < 0):
                number = -ele 
            if(A[number] < 0):
                return number
            else:
                A[number] = -1 * A[number] 
        
        return -1
