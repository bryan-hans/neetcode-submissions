class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for letter in word:
                position = ord("a") - ord(letter)
                count[position] += 1 
            res[tuple(count)].append(word)
        return list(res.values())
        
