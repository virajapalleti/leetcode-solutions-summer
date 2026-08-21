class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        original = {}

        for num in nums:
            if num in original:
                return num
            else:
                original[num] = True
