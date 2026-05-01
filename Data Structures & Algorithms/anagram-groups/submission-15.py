class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)

        for word in strs:
            letter_count = [0] * 26
            for c in word:
                position = ord(c) - ord("a")
                letter_count[position] += 1 
            results[tuple(letter_count)].append(word)
        return list(results.values())     