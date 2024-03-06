import string
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = dict.fromkeys(string.ascii_lowercase, 0)
        for char in magazine:
            count[char] = count.get(char, 0) + 1
        #print(count)

        for c in ransomNote:
            if count[c] > 0:
                count[c] -= 1
            else:
                return False
        return True
