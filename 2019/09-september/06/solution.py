class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
    # Fill this in.
    if root_node == None:
        return floor, ceil

    if root_node.value == k:
        return k, k

    # Candidate for a new floor
    if root_node.value < k:
        if floor == None or (k - root_node.value) < (k - floor):
            floor = root_node.value

    # Candidate for a new ceil
    if root_node.value > k:
        if ceil == None or (root_node.value - k) < (ceil - k):
            ceil = root_node.value

    # Now find the floor and ceil of children
    left_floor, left_ceil = findCeilingFloor(root_node.left, k, floor, ceil)
    right_floor, right_ceil = findCeilingFloor(root_node.right, k, floor, ceil)

    # min(None, x) is None, which is not what we want. So if we have a ceil that
    # is None, assign the value of the other ceil to it.
    if right_ceil == None:
        right_ceil = left_ceil
    elif left_ceil == None:
        left_ceil = right_ceil

    # We now either have:
    #  - 2 Nones
    #  - 2 identical numbers
    #  - 2 different numbers
    # All of which are now acceptable

    ceil = min(left_ceil, right_ceil)

    floor = max(left_floor, right_floor)

    return floor, ceil



root = Node(8)
root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)

print findCeilingFloor(root, 0) == (None,2)
print findCeilingFloor(root, 1) == (None,2)
print findCeilingFloor(root, 2) == (2,2)
print findCeilingFloor(root, 3) == (2,4)
print findCeilingFloor(root, 4) == (4,4)
print findCeilingFloor(root, 5) == (4,6)
print findCeilingFloor(root, 6) == (6,6)
print findCeilingFloor(root, 7) == (6,8)
print findCeilingFloor(root, 8) == (8,8)
print findCeilingFloor(root, 9) == (8,10)
print findCeilingFloor(root, 10) == (10,10)
print findCeilingFloor(root, 11) == (10,12)
print findCeilingFloor(root, 12) == (12,12)
print findCeilingFloor(root, 13) == (12,14)
print findCeilingFloor(root, 14) == (14,14)
print findCeilingFloor(root, 15) == (14,None)
print findCeilingFloor(root, 16) == (14,None)
print findCeilingFloor(root, 17) == (14,None)
