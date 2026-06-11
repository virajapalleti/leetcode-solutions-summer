class Solution:
    def frequencySort(self, s: str) -> str:

        frequency = Counter(s)
        sorted_freq = frequency.most_common()

        result =[]
        for letter,count in sorted_freq:
            result.append(letter * count)
        
        return "".join(result)