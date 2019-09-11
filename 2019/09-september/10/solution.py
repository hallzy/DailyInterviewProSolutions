def findPythagoreanTriplets(nums):
    # Fill this in.

    # We will sort the array, so that we can treat the larger numbers as the
    # sums easier
    nums.sort()

    # Find the squares now
    for idx in range(0, len(nums)):
        nums[idx] **= 2

    # c can be any of the numbers except for the first 2, because the first 2
    # must be the operands
    for c in range(2, len(nums)):
        a = 0
        b = c - 1

        while nums[a] < nums[b]:
            if nums[a] + nums[b] == nums[c]:
                return True

            if nums[a] + nums[b] < nums[c]:
                a += 1
            else:
                b -= 1
    return False


print findPythagoreanTriplets([3, 12, 5, 13]) == True
print findPythagoreanTriplets([1,2]) == False
print findPythagoreanTriplets([1,2,3]) == False
print findPythagoreanTriplets([1,2,3,4]) == False
print findPythagoreanTriplets([1,2,3,4,5]) == True
