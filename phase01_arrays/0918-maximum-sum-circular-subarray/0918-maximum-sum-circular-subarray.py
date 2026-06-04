class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max = nums[0]
        global_max = nums[0]
        
        cur_min = nums[0]
        global_min = nums[0]
        
        total_sum = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            # 1. Kadane's for Maximum
            cur_max = max(num, cur_max + num)
            global_max = max(global_max, cur_max)
            
            # 2. Inverted Kadane's for Minimum
            cur_min = min(num, cur_min + num)
            global_min = min(global_min, cur_min)
            
            total_sum += num
            

        if global_max < 0:
            return global_max

        return max(global_max, total_sum - global_min)