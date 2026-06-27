class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        longest = ""
        
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                
                if len(substring) > len(longest):
                    
                    char_set = set(substring)
                    is_nice = True
                    
                    for char in char_set:
                        if char.lower() not in char_set or char.upper() not in char_set:
                            is_nice = False
                            break 
                    
                    if is_nice:
                        longest = substring
                        
        return longest