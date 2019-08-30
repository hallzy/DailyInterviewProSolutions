class Solution:
    def longestPalindrome(self, s):
        # Fill this in.
        idx = end = start = 0

        longest = ""

        # Single char is also a palindrome, so start with the first character
        current = s[0]

        while idx < len(s):
            start -= 1
            end += 1

            if start < 0 or end >= len(s) or s[start] != s[end]:
                idx += 1
                start = end = idx
                if idx < len(s):
                    current = s[idx]
                continue
            current = s[start] + current + s[end]

            if len(current) > len(longest):
                longest = current
        return longest



# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar
