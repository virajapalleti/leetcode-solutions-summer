class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = "".join(char for char in s if char.isalnum() ).lower()
        pointer1 = 0
        pointer2 = (len(cleaned_s)-1)
        while(pointer1 < pointer2):
            if cleaned_s[pointer1] == cleaned_s[pointer2]:
                pointer1 += 1
                pointer2 -= 1
            else:
                return False
        
        return True


