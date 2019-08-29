## NOTE: Space and time complexity are Linear
# - Only loops through the string once
# - Worst case space is if memo fills up to the length of the input string

class Solution:
  def lengthOfLongestSubstring(self, s):
    # Fill this in.


    # The current string
    memo = {}

    # The length of the longest string we have found
    longest = 0

    # Loop through the input string
    for c in s:
      # If the character is not in the dictionary, then add it
      if c not in memo:
        memo[c] = 1
        continue

      # if char was in the memo, then it is a repeat...

      # Get the size of the memo
      length = len(memo)

      # set the new longest count
      longest = length if length > longest else longest

      # reset memo
      memo = {}

    # return the longest substring length
    return longest

print Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx')
# 10
