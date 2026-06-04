class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum = 0

        for i in range(n):
            sum += nums[i]
            nums[i] = sum


        return nums

