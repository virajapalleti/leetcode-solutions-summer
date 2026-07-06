from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for word in strs:
            signature = "".join(sorted(word))
            
            
            anagram_map[signature].append(word)
            
        return list(anagram_map.values())