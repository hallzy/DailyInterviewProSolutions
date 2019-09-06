def check(lst):
    # Fill this in.
    outOfOrderCount = 0

    idx = 0
    while idx < len(lst) - 1:
        if lst[idx] > lst[idx+1]:
            if outOfOrderCount != 0:
                return False
            outOfOrderCount = 1
        idx += 1
    return True



print check([13, 4, 7]) == True
print check([5,1,3,2,5]) == False
