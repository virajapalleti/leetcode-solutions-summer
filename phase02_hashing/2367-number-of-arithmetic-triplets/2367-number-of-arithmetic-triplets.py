class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        
        for num in nums:
            one = num + diff
            two = one + diff
            if one in nums and two in nums:
                count = count + 1
        return count



        # omg i love this, such an easy answer yey