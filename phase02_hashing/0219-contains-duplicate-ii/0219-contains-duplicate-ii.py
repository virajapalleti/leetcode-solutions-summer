class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # using dict= { number : last_seen_index }

        original = {}

        for i in range(len(nums)):
            v = nums[i]

            if v in original and i - original[v] <= k:
                return True

            original[v] = i

        return False