from collections import Counter
def longestPalindrome(self, s: str) -> int:
    count = Counter(s)
    num = 0
    for x in count.values():
        num += x // 2 * 2
        if x % 2 == 1 and num % 2 == 0: # second is to check if there is a unique center yet
            num += 1
    return num

# set solution
def longestPalindrome(self, s: str) -> int:
    hash = set()
    for c in s:
        if c not in hash:
            hash.add(c)
        else:
            hash.remove(c)
    # len(hash) is the number of the odd letters
    return len(s) - len(hash) + 1 if len(hash) > 0 else len(s) # if there is odd characters, s - num_odd + 1.