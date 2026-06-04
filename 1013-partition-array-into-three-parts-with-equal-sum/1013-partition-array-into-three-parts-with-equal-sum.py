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
