class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping the frequency of characters to each word
        # {(char freq map : words}
        # frequency map for each word in s
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            # use the frequency as the key and append the word to this frequncy
            res[tuple(count)].append(s)
        # return the values which are the words we are storing in the freq map
        return list(res.values())