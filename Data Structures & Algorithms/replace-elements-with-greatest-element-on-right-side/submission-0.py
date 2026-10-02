class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr) # n: var len of arr
        rightMax= -1 # rightMax: var initialize on -1
        ans = [0] * n # ans: array of answers initializes of the same size with 0´s

        #loop with range, staring from last element to the firts range(n-1, -1, -1)
        for i in range(n-1, -1, -1):
            ans[i] = rightMax # replace ans[i] with rightMax
            rightMax = max(arr[i], rightMax) # update rightMax with the max between arr[i] and rightMax

        return ans
