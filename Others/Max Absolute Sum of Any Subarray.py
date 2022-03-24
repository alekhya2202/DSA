#https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prevMin = 0
        prevMax = 0
        sz = len(nums)
        s = 0
        i = 0
        result = 0
        while i < sz:
            s += nums[i]
            i += 1
            result = max(result, abs(s - prevMin), abs(s - prevMax))
            prevMin = min(prevMin, s)
            prevMax = max(prevMax, s)
        return result
