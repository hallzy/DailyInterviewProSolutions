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

            # Ensure that start and end are still valid.
            # If the surrounding elements don't match then reset
            if start < 0 or end >= len(s) or s[start] != s[end]:
                # Increment our string counter
                idx += 1

                # Reset start to be the same as the string counter
                start = idx

                # If the idx is valid, use that character as our string
                if idx < len(s):
                    current = s[idx]

                # If the character at the string counter is equivalent to the
                # next character, add it to the current string This is what
                # handles the case where we have an even length string with 2
                # identical middle characters
                if idx + 1 < len(s) and s[idx+1] == s[idx]:
                    current += s[idx]
                    idx += 1

                # Now set the end, which may be different from start of the
                # previous if statement triggered
                end = idx
                continue
            current = s[start] + current + s[end]

            if len(current) > len(longest):
                longest = current
        return longest



# Test program
print(str(Solution().longestPalindrome("million") == "illi"))
print(str(Solution().longestPalindrome("millions") == "illi"))
print(str(Solution().longestPalindrome("tracecar") == "racecar"))
print(str(Solution().longestPalindrome("tracecars") == "racecar"))
print(str(Solution().longestPalindrome("bananas") == "anana"))
print(str(Solution().longestPalindrome("banana") == "anana"))
