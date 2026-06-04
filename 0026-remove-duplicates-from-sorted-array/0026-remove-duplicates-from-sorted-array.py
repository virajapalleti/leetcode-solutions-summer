class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:
            return 0 ##for when array is empty

        k = 1 
        for i in range(1, len(nums)):
            
            if nums[i] != nums[i - 1]: #its a new number so place at k and inc k
                nums[k] = nums[i]
                k += 1
                
        return k #k=unique elements