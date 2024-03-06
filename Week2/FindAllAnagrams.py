class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = len(p)
        compStr = sorted(p)
        #print(compStr)
        res = []
        for i in range(0, len(s)):
            #print(i)
            subStr = sorted(s[i:i+l])
            #print(subStr)
            if subStr == compStr:
                res.append(i)

        return res
