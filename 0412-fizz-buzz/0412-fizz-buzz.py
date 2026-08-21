class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [0] * n

        for i in range(n):
            num = i + 1  

            if num % 3 == 0 and num % 5 == 0:
                answer[i] = "FizzBuzz"
            elif num % 3 == 0:
                answer[i] = "Fizz"
            elif num % 5 == 0:
                answer[i] = "Buzz"
            else:
                answer[i] = str(num)
        return answer
