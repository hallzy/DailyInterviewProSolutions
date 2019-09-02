# O(n) time complexity as we loop through the nums array twice, but one after
# another, and all other operations are constant time

# O(1) space complexity because all variables use constant space except for the
# input array


# The problem specifies specifically 3 unique numbers and that those 3 numbers
# are always 1, 2, and 3, which simplifies the solution a lot.

def sortNums(nums):
    # Fill this in.
    count = [0,0,0]

    for num in nums:
        # Indices are 0,1,2, but unique vals are 1,2,3... subtract 1 from
        # whatever num is
        count[num - 1] += 1

    # Track the index of nums
    idx = 0

    # Track the index of count
    countIdx = 0

    # Loop through the nums array
    while idx < len(nums):
        # If the count for the current count index is 0, then we have exhausted
        if count[countIdx] == 0:
            # this number. Try next number now
            countIdx += 1
            continue
        # The number is 1 more than the index, so replace this idx for nums with
        # the count index
        nums[idx] = countIdx + 1

        # take off a count for this index
        count[countIdx] -= 1
        # Increment nums index
        idx += 1
    return nums



print sortNums([3, 3, 2, 1, 3, 2, 1])
# [1, 1, 2, 2, 3, 3, 3]
