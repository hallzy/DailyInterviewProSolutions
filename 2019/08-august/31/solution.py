class Solution:
    def getRange(self, arr, target):
        # Fill this in.
        firstIdx = -1
        lastIdx = -1

        start = 0
        end = len(arr) - 1

        # Binary search for the first occurrence
        while start <= end:
            middle = start + (end - start) // 2
            if(( middle == 0 or target > arr[middle - 1]) and arr[middle] == target):
                firstIdx = middle
                break
            elif target > arr[middle]:
                start = middle + 1
            else:
                end = middle - 1


        start = 0
        end = len(arr) - 1

        # Binary search for the last occurrence
        while start <= end:
            middle = start + (end - start) // 2
            if ((middle == (len(arr) - 1) or target < arr[middle + 1]) and arr[middle] == target):
                lastIdx = middle
                break
            elif target < arr[middle]:
                end = middle - 1
            else:
                start = middle + 1


        return [firstIdx, lastIdx]



# Test program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
print(Solution().getRange(arr, x) == [1,4])

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 10
print(Solution().getRange(arr, x) == [-1, -1])

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 8
print(Solution().getRange(arr, x) == [8,9])

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 1
print(Solution().getRange(arr, x) == [0,0])

arr = [1,2,3]
x = 1
print(Solution().getRange(arr, x) == [0,0])
