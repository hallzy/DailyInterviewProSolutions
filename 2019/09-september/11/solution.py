def distance(s1, s2):
    # Fill this in.
    s1Len = len(s1)
    s2Len = len(s2)

    # Initialize a 2d map which will keep track of the fewest number of edits
    # needed (map[i]j]) for length of s1 and s2, i and j
    map = [[0 for x in range(s2Len+1)] for x in range(s1Len+1)]

    # Loop through all indices of string 1
    for i in range(s1Len+1):
        # Loop through all indices of string 2
        for j in range(s2Len+1):
            # If the current index for string 1 is 0, then we have reached the
            # end of string 1, so any characters left in string 2 need to be
            # removed. So the number of edits at [i][j] is j
            if i == 0:
                map[i][j] = j
                continue

            # Same as previous, but if we finish string 2
            if j == 0:
                map[i][j] = i
                continue

            # If the previous characters equalled, then the edit count for
            # [i][j] hasn't changed since last characters
            if s1[i-1] == s2[j-1]:
                map[i][j] = map[i-1][j-1]
                continue

            # Pretend to add a character. Simulate by taking a character from
            # second string
            add = map[i][j-1]

            # Pretend to remove a character. Simulate by taking a character from
            # first string
            delete = map[i-1][j]

            # Pretend to change a character. Simulate by looking at the edit
            # count for the previous character
            edit = map[i-1][j-1]

            # Find the shorted edit distance between adding, removing, and
            # editing, and add 1 to it for the current change
            map[i][j] = 1 + min(add, delete, edit)

    return map[s1Len][s2Len]

print distance('biting', 'sitting') == 2
print distance('steven', 'stephen') == 2
print distance('steve', 'stephen') == 3
