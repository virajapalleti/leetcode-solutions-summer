class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        original = set()

        for num in nums:
            if num in original:
                return True
            
            else:
                original.add(num)

        return False