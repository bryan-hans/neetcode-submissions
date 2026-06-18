class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)

        for word in strs:
            letters = [0] * 26
            for c in word: 
                position = ord(c) - ord('a')
                letters[position] += 1 
            results[tuple(letters)].append(word)
        return list(results.values())

