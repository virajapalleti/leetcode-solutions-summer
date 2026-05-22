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

## 560. Subarray Sum Equals K (without hashmap, thus time limit exceeded for large arrays)

```
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
```

Solution: Python

```
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        prefixSum = [0] * n
        prefixSum[0] = nums[0]

        for i in range(1, n):
            prefixSum[i] = prefixSum[i - 1] + nums[i]

        total_subarrays = 0

        for i in range(n):
            for j in range(i, n):

                if i == 0:
                    subarray_sum = prefixSum[j]
                else:
                    subarray_sum = prefixSum[j] - prefixSum[i - 1]

                if subarray_sum == k:
                    total_subarrays += 1

        return total_subarrays
```

## 53. Maximum Subarray ★★

```
Given an integer array nums, find the subarray with the largest sum, and return its sum.
```

Solution: Python

```
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        totalsum = nums[0]
        tempsum = nums[0]

        for i in range(1, len(nums)):
            tempsum = max(nums[i], nums[i]+tempsum)
            totalsum = max(totalsum, tempsum)

        return totalsum
```

## 121. Best Time to Buy and Sell Stock

```
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
```

Solution: Python

```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for i in range (1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit
```

## 122. Best Time to Buy and Sell Stock II

```
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.

Find and return the maximum profit you can achieve
```

Solution: Python

```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totprofit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                totprofit += prices[i] - prices[i - 1]
                    ##actually simpler than the previous, as just add it to total prfit, if any fo the next elements are greater than current
        return totprofit

```

## 238. Product of Array Except Self ★★★★

```
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

Solution: Python

```
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        answer = [1] * len(nums)

        ##prefix[0] = nums[0]
        ##suffix[len(nums)-1] = nums[len(nums) -1]

        for i in range (1, len(nums)):
            prefix[i] = prefix [i-1] * nums[i-1] ##prof of evrything before the i and after the i, then their prod = answer
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        for i in range (0, len(nums)):
            answer[i] = prefix[i] * suffix[i]

        return answer
```
## 152. Maximum Product Subarray
```
Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
Note that the product of an array with a single element is the value of that element.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```
Solution: Python
```
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            temp_max = max(num, num * cur_max, num * cur_min)
            cur_min = min(num, num * cur_max, num * cur_min)
            cur_max = temp_max
            
            global_max = max(global_max, cur_max)

        return global_max
```