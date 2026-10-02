class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = res = 0
        for num in nums:
            if num != 0:
                count += 1 # if is 1 we increment the count
            else:
                res = max(res, count)
                count = 0
        
        return max(res, count)
        