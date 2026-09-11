class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            count = [0] * 26
            
            for letter in word:
                position = ord(letter) - ord('a')
                count[position] += 1
            anagrams[tuple(count)].append(word)
        return list(anagrams.values())
