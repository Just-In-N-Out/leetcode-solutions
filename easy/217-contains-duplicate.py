# 217. Contains Duplicate
# Difficulty: Easy
# Time: O(n), Space: O(n)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:
                return True
            else:
                seen.add(x)
        return False
