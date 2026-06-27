class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0 
        sum = 0
        min_length = float('inf')

        for right in range(len(nums)):
            sum += nums[right]
            
            while sum >= target:
                min_length = min(min_length, right - left + 1)
                
                sum -= nums[left]
                left += 1

        if min_length != float('inf'):
            return min_length
        else:
            return 0