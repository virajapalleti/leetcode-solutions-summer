class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        original = {}  

        for i, num in enumerate(nums):
            if target - num in original:
                return [original[target - num], i]
            
            original[num] = i
            
        return []