class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # count the frequency of the characters in each word 
        # group words with the same frequency of characters in a sublist

        # hashmap -> {(character frequency a-z): [[sublists]]}
        # KEY character frequency array: [0, .. , 1]
        # using ascii values and normalizing to 0-26

        anagrams = defaultdict(list)

        # count the frequency of the characters in each word 
        for s in strs:
            freq = [0]*26 
            # count all characers in the string
            for c in s:
                freq[ord(c) - ord("a")] += 1
            # append the word s to that freq key, use tuple as key value
            anagrams[tuple(freq)].append(s)

        # print(anagrams.values()) returns the dict values object -> cast to list
        
        return list(anagrams.values())