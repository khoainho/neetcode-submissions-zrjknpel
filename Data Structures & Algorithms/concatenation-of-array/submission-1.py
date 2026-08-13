class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        answer = []

        for i in range(2):
            for n in nums:
                answer.append(n)
            
        return answer