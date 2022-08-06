from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        num = 0
        for x in count.values():
            num += x // 2 * 2
            if x % 2 == 1 and num % 2 == 0: # second is to check if there is a unique center yet
                num += 1
        return num