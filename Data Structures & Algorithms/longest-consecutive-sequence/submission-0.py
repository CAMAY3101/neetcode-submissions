class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_s = set(nums) #[2,20,4,10,3,5]
        long = 0

        for num in nums_s: 
            if num - 1 not in nums_s: # A number is the start of a sequence if num - 1 is not in the set.
                length = 1
                while num + length in nums_s:
                    length += 1
                long = max(length, long)
                
        return long

        