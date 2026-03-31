class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = collections.Counter(s)
        countT = collections.Counter(t)

        return countS == countT
        