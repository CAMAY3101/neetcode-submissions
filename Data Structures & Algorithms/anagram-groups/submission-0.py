class Solution:        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # aux = {'act': ['act',],'post': ['pots', 'tops'], 'act': [cat,]}
        # defaultdict() create a dictionary with empty set kind of value (in this case an empty list)
        res = defaultdict(list) # dict that we return with defualt empty list

        # iterate througt every string on the list
        for s in strs:
            count = [0] * 26 # help us to generate the key to identificate another anagram by knowing which elements
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())