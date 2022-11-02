class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        i = 0
        while i < len(chars):
            j = i + 1
            while j < len(chars) and chars[i] == chars[j]:
                j += 1
            if j - i > 1:
                chars[i + 1:j] = list(str(j - i))
            i = j
        return len(chars)
