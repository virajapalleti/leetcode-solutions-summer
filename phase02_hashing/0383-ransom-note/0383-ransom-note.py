class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        tally = {}
        
        for letter in magazine:
            tally[letter] = tally.get(letter, 0) + 1
            
        for letter in ransomNote:
            if tally.get(letter, 0) == 0:
                return False
            tally[letter] -= 1
            
            
        return True