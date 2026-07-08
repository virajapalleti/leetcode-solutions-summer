import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        min_speed = right

        while left <= right:
            mid = (left + right ) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil (pile / mid)
            if hours <= h: ## means her time is fast enough, could be too big, so we moved left
                min_speed = mid

                right = mid - 1
            else:
                left = mid + 1

        return min_speed 