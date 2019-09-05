def singleNumber(nums):
    # Fill this in.
    result = 0
    for val in nums:
        result ^= val
    return result

print singleNumber([4, 3, 2, 4, 1, 3, 2]) == 1
print singleNumber([1]) == 1
print singleNumber([2]) == 2
print singleNumber([2,2,3]) == 3
print singleNumber([4,2,2]) == 4
