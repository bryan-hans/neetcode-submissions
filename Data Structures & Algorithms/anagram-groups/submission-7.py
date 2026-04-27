class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        results = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for character in word:
                count[ord(character) - ord("a")] += 1
            results[tuple(count)].append(word)
        return list(results.values())