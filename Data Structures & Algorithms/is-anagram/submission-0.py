class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create a frequency map of chars 
        # use two hashmaps and compare them
        # char : freq
        s_freq, t_freq = {}, {}

        # check if same length first
        if len(s) != len(t):
            return False

        # frequency map
        for i in range(len(s)):
            s_freq[s[i]] = 1 + s_freq.get(s[i], 0)
            t_freq[t[i]] = 1 + t_freq.get(t[i], 0)
        
        return s_freq == t_freq


        
        
        
        