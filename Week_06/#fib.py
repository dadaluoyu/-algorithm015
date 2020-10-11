#fib
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n
        a = [0, 1]
        for i in range(n):
            a[i & 1] = (a[0] + a[1]) % (int)(1e9 + 7)
        return a[n & 1]