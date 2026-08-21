class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        final_num = nums * 2
        k = k % n


        for i in range(n):
            nums[i] = final_num[n - k + i]
        
        return final_num