# Inutition: count each letter, all must have even number except 1 in center

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = dict()
        for c in s:
            count[c] = count.get(c, 0) + 1
        print(count)

        total = 0
        odd = 0

        for val in count.values():
            if val % 2 == 0:
                total += val
            else:
                total += val - 1
                odd = 1

        return total + odd
