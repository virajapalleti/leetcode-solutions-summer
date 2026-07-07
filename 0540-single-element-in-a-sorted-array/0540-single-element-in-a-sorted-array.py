class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left+right) // 2

            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    left = mid + 2 #as its a valid pair, we can discard the left and focus on the right half
                else:
                    right = mid #discard right and focus on left half

            else:
                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                else:
                    right = mid - 1

        return nums[left]

        # USED INDEX PARITY