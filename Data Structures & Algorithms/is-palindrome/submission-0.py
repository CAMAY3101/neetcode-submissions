class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.split())
        size = len(s)
        l, r = 0, size-1

        #tabacat!

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            elif not s[r].isalnum():
                r -= 1
                continue

            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False  

        return True