# Arrays

## 1929. Concatenation of Array

```
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
Specifically, ans is the concatenation of two nums arrays. Return the array ans.

Example 1:
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
ans = [1,2,1,1,2,1]
```

Solution:
Python

```
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # make a new array ans with 2n elements, all initialized to 0
        ans = [0] * (2 * n)

        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]

        return ans
```

## 1480. Running Sum of 1d Array

```
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
```

Solution:
Python

```
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum = 0

        for i in range(n):
            sum += nums[i]
            nums[i] = sum

        return nums

```
