class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = []

        for n in nums:
            if n in visited:
                return True
            else:
                visited.append(n)

        return False

        


    



        
            
