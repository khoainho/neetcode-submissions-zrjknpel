class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()

        for i in nums:
            if i in hashmap:
                return True
            else:
                hashmap.add(i)

        return False
            
     
            
        


    



        
            
