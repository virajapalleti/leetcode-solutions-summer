class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        totalsum = sum(nums)
        leftsum =0
        rightsum =0

        for i in range (0, len(nums)) :
            rightsum = totalsum - leftsum - nums[i]

            if rightsum == leftsum:
                return i
            
            leftsum += nums[i]

        return -1