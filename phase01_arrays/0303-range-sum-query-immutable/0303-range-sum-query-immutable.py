class NumArray:

    def __init__(self, nums: List[int]):
        sum = 0
        self.prefix = [0] * len(nums)

        for i in range (0, len(nums)):
            sum += nums[i]
            self.prefix[i] = sum

    def sumRange(self, left: int, right: int) -> int:
        if (left == 0):
            return self.prefix[right]
        else:
            return self.prefix[right] - self.prefix[left-1] 



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)