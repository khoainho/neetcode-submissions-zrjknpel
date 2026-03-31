class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper (x, n):
            if x == 0: return 0
            # 0 to the power of anything is still 0
            if n == 0: return 1
            # anything to the power of 0 is 1

            res = helper( x, n // 2)
            # half
            res = res * res
            return x * res if n % 2 else res

        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res