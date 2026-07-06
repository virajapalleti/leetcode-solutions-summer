class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for num in range(len(nums)):
            if nums[num] == target:
                return num
            elif nums[num] > target:
                return num
        
        return len(nums)