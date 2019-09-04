def two_sum(list, k):
    # Fill this in.
    # Keep track of values we have passed in the list
    hash = {}

    # Loop through the list
    for val in list:
        # if the target - current value is a key in the hash, then that means
        # that 2 numbers in the list add to k.
        if (k - val) in hash:
            return True
        # If not found, then add it
        hash[val] = True
    return False

print two_sum([4,7,1,-3,2], 5) == True
print two_sum([4,7,1,-3,2], 11) == True
print two_sum([4,7,1,-3,2], 1) == True
print two_sum([4,7,1,-3,2], 6) == True
print two_sum([4,7,1,-3,2], 8) == True
print two_sum([4,7,1,-3,2], 4) == True
print two_sum([4,7,1,-3,2], -2) == True
print two_sum([4,7,1,-3,2], -1) == True
print two_sum([4,7,1,-3,2], 4) == True
print two_sum([4,7,1,-3,2], 7) == False
