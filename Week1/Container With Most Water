class Solution:
    def maxArea(self, height: List[int]) -> int:
        curr_max = 0
        for n in range(0, len(height)):
            for m in range(n+1, len(height)):
                curr_max = max(min(height[n], height[m]) * (m-n), curr_max)
        return curr_max
