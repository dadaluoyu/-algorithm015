#lc 367 完全平方数判断
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num
        mid = 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == num:
                return True
            if mid * mid > num:
                right = mid - 1
            else:
                left = mid + 1 
        return mid * mid == num