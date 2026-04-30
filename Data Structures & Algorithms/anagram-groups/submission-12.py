class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)

        for string in strs:
            letters = [0] * 26
            for char in string:
                position = ord(char) - ord("a")
                letters[position] += 1 
            results[tuple(letters)].append(string)
        return list(results.values())


