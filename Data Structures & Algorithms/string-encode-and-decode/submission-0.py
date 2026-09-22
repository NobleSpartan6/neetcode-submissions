class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            n = len(s)
            encoded += str(n) + "#" + s
        return encoded


    def decode(self, s: str) -> List[str]:
        words = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length 

            # grab the word and add to the list
            words.append(s[i:j])

            # move pointers to next word 
            i = j
        # once we get through string return decoded list of words
        return words