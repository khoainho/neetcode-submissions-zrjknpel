class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += str(len(i)) + "!" + i
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 
        while i < len(s):
            j = i 
            while s[j] != "!":
                j += 1
            charCount = int(s[i:j])
            res.append(s[j + 1 : j + 1 + charCount])

            i = j + 1 + charCount
        return res

