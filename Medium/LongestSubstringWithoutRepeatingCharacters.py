class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        i = 0
        j = 0
        max_len = 0
        while i < len(s) and j < len(s):
            if s[j] not in hashset:
                hashset.add(s[j])
                j += 1
                max_len = max(max_len, j - i)
            else:
                hashset.remove(s[i])
                i += 1
        return max_len
