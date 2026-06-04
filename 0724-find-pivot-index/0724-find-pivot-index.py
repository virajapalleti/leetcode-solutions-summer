class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalsum = sum(nums)
        sum1 =0
        sum2=0

        for i in range (0, len(nums)):
            
            sum2 = totalsum - sum1 - nums[i]

            if sum1 == sum2:
                return i

            sum1 += nums[i]

        return -1