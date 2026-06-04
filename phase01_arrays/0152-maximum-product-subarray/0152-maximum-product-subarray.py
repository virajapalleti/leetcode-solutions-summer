class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            temp_max = max(num, num * cur_max, num * cur_min)
            cur_min = min(num, num * cur_max, num * cur_min)
            cur_max = temp_max
            
            global_max = max(global_max, cur_max)

        return global_max