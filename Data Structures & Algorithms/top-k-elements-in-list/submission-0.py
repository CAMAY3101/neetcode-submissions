class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}

        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1

        sort_freq = dict(sorted(frequencies.items(), key= lambda item:item[1], reverse=True))
        res = []
        for index, (key, value) in enumerate(sort_freq.items()):
            if index > k -1:
                break
            else:
                res.append(key)

        return res
            

            