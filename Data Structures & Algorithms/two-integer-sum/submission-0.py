class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        existing = {} # value : position
        for idx, value in enumerate(nums):
            search = target - value
            if search in existing:
                return [existing[search], idx]
            else:
                existing[value] = idx


