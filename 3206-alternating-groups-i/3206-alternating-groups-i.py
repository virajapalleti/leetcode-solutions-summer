class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        count = 0
        
        for i in range(n):
            
            first = colors[i]
            second = colors[(i + 1) % n]
            third = colors[(i + 2) % n]
            
            if first != second and second != third:
                count += 1
                
        return count