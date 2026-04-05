class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:                
        def can_split(largest):
            subarray = 0
            curr_sum = 0

            for n in nums:
                curr_sum += n
                if curr_sum > largest:
                    subarray += 1
                    curr_sum = n
                
            return subarray + 1 <= k

        l, r = max(nums), sum(nums)
        res = r

        while l <= r:
            mid = (l + r) // 2
            if can_split(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res
