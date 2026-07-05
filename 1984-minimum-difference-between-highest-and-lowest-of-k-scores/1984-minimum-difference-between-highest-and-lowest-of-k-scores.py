class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
            
        nums.sort()
        
        min_diff = float('inf')
        for i in range(len(nums) - k + 1):
            
            highest = nums[i + k - 1]
            lowest = nums[i]
            
            min_diff = min(min_diff, highest - lowest)
            
        return min_diff