class Solution:
  def isValid(self, s):
    # Fill this in.
    stack = []

    # Mapping of opening brackets to corresponding closing brackets
    mapping = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    for c in s:
        # If current char is a key, it is an opening bracket, so push to stack
        if c in mapping.keys():
            stack.append(c)
        # If current char is a value, it is a closing bracket.
        elif c in mapping.values():
            # Pop off the last opening bracket
            popped = stack.pop()
            # Does the popped opening bracket match the closing bracket?
            if mapping[popped] != c:
                # If not, then fail
                return False
        # Else case is any other character, Which I don't care about

    # Stack must be empty
    return len(stack) == 0

# Test Program
print(Solution().isValid("()(){(())") == False)
print(Solution().isValid("") == True)
print(Solution().isValid("([{}])()") == True)
print(Solution().isValid("I (am {testing (this [now])})") == True)
print(Solution().isValid("I (am {testing (this) [now])})") == False)
print(Solution().isValid("I (am {testing (this} [now])})") == False)
