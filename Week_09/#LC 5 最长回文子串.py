#LC 5 最长回文子串

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return
        n = len(s)
        isPalindrome = [[False] * n for _ in range(n)]
        isPalindrome[0][0] = True
        for i in range(1, n):
            isPalindrome[i][i] = True
            isPalindrome[i][i - 1] = True
        
        start, longest = 0, 1
        for length in range(1, n):
            for i in range(n - length):
                j = i + length
                isPalindrome[i][j] = (s[i] == s[j]) and isPalindrome[i + 1][j - 1]
                if isPalindrome[i][j] and length + 1 > longest:
                    longest = length + 1
                    start = i
        return s[start: start + longest]