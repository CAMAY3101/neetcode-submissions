class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums) # 4
        ans = [0] * (2 * n)

        for i in range(n):
            ans[i] = ans[i + n] = nums[i]

        return ans


        