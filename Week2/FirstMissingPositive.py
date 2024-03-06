# intuition: can't sort, would take O(n log n)
# also can't build a list or dict of "seen" variables, O(n) space if all ints are unique
# should disregard all numbers smaller than smallest unseen integer

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        curr = 1
        n = 0
        #for n in range(end):
        while n < len(nums):
            print("n: ", n)
            print(nums[n])
            if nums[n] < curr:
                nums.pop(n)
                n -= 1
                #end -= 1
            elif nums[n] == curr:
                curr += 1
                n = 0
                continue
            n += 1
            print("curr: ", curr)
        return curr

  # Currently passes 171/176 tests
