class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1 
        # L = 0
        # R = 5
        
        while L <= R:
            # L = 0 3 3
            # R = 5 5 3
            mid = (L + R) // 2 # 2 4 3

            # 2 == 4
            # 6 == 4
            # 4 == 4
            if nums[mid] == target:
                return mid
            # 2 > 4
            # 6 > 4
            elif nums[mid] > target:
                R = mid - 1 # R = 3
            # 2 < 4
            # 6 < 4
            elif nums[mid] < target:
                L = mid + 1 # L = 3
        
        return -1
