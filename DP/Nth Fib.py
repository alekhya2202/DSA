#https://leetcode.com/problems/fibonacci-number/
class Solution:
    def __init__(self):
        self.fib_dic = {}
        
    def fib(self, n: int) -> int:
        if n in self.fib_dic: 
            return self.fib_dic[n]
        
        if n == 0: 
            return 0
        
        if n <= 2: 
            return 1
        
        res = self.fib(n-1) + self.fib(n-2)
        self.fib_dic[n] = res
        
        return res
