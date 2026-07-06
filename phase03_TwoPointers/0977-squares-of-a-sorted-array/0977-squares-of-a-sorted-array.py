class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        insert = len(result) - 1

        while left <= right:
            if nums[left] * nums[left] > nums[right] * nums[right]:
                result[insert] = nums[left] * nums[left]
                insert -= 1
                left += 1
            else:
                result[insert] = nums[right] * nums[right]
                right -= 1
                insert -=1
        return result