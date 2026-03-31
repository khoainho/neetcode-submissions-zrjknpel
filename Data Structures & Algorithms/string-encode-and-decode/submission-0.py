class Solution:

    def encode(self, strs: List[str]) -> str:
        combine = ""
        for i in strs:
            combine += str(len(i)) + "#" + i
        return combine

    def decode(self, s: str) -> List[str]:
        decode = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1 
            length = int(s[i:j])
            decode.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return decode

                
        