#https://www.interviewbit.com/problems/subset/

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        def combi(A, B):
            l = []
            if B == 0:
                return []
            if B == 1:
                for i in A:
                    l.append([i])
                return l
            else:
                for i in range(len(A) - B + 1):
                    x = [A[i]]
                    xs = A[i + 1:]
                    for j in combi(xs, B - 1):
                        l.append(x + j)
                return l
                
        l = []
        A.sort()
        for B in range(len(A)):
            for i in combi(A, B+1):
                l.append(i)
        l.append([])
        return sorted(l)
