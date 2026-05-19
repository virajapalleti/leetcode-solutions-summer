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

Time complexity: O(n)
Space complexity: O(1)
```

## 303. Range Sum Query - Immutable ★★

```
Given an integer array nums, handle multiple queries of the following type:
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:
NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Example 1:
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]
Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
```

Solution:
Python

```
class NumArray:

    def __init__(self, nums: List[int]):
        sum = 0
        self.prefix = [0] * len(nums)
            #new array with length as nums and all elements set to 0

        for i in range (0, len(nums)):
            sum += nums[i]
            self.prefix[i] = sum
                #this new array's ach element is sum of 1th elements in nums array

    def sumRange(self, left: int, right: int) -> int:
        if (left == 0):
            return self.prefix[right]
        else:
            return self.prefix[right] - self.prefix[left-1]
                #basically means that
                for sum[5,2] = sum at 5th position - sum at 1st position
```

## 724. Find Pivot Index

```
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.
```

Solution: Python

```
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalsum = sum(nums)
        sum1 =0
        sum2 =0
            #2 sums, one for left side and one for right, to compare
        for i in range (0, len(nums)):

            sum2 = totalsum - sum1 - nums[i]

            if sum1 == sum2:
                    #we comapre before adding as the current element should not be included in the sums
                return i

            sum1 += nums[i]
                #if case doesnt satisfy, we add the current element and move forward

        return -1
```

## 1013. Partition Array Into Three Parts With Equal Sum

```
Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.
Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])
```

Solution: Python

```
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        sum1 =0
        totalsum = sum(arr)
        parts=0

        if totalsum % 3 != 0:
            return False

        for i in range (0, len(arr)):
            sum1 += arr[i]
            if sum1 == totalsum // 3:
                parts +=1
                sum1 = 0
            if parts >= 3:
                return True
        return False

```

## 26. Remove Duplicates from Sorted Array

```
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.
The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.
```

Solution: Python

```
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
```
