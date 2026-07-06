class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        char_count = {}
        max_length = 0
        
        for right in range(len(s)):
            char = s[right]
            
            char_count[char] = char_count.get(char, 0) + 1
            
            while char_count[char] > 2:
                char_count[s[left]] -= 1
                
                left += 1
                
            max_length = max(max_length, right - left + 1)
            
        return max_length