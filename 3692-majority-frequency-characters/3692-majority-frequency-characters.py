class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        counts = Counter(s)

        freq_groups = defaultdict(list)
        for char, freq in counts.items():
            freq_groups[freq].append(char)

        best_k = max(freq_groups.keys(), key=lambda k: (len(freq_groups[k]), k))

        return "".join(freq_groups[best_k])