class Solution:
    def getRange(self, arr, target):
        # Fill this in.
        # Do binary search to find the number
        idx = self.binarySearch(arr, target)

        if idx == -1:
            return False

        first = idx
        last = idx

        while first - 1 >= 0 and arr[first-1] == arr[idx]:
            first -= 1

        while last + 1 < len(arr) and arr[last+1] == arr[idx]:
            last += 1

        return [first,last]

    def binarySearch(self, arr, target):
        start = 0
        end = len(arr) - 1

        while start <= end:
            middle = start + (end - start) / 2
            if target == arr[middle]:
                return middle
            elif target < arr[middle]:
                end = middle - 1
            else:
                start = middle + 1
        return -1


# Test program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
print(Solution().getRange(arr, x) == [1,4])

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 10
print(Solution().getRange(arr, x) == False)

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 8
print(Solution().getRange(arr, x) == [8,9])

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 1
print(Solution().getRange(arr, x) == [0,0])

arr = [1,2,3]
x = 1
print(Solution().getRange(arr, x) == [0,0])
