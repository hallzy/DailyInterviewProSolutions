# NOTE: This solution has linear time and space complexity

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    # Fill this in.

    # Get the value of the given nodes
    val = l1.val + l2.val + c

    # Get a carry if one exists
    carry = val // 10

    # Get the value without the carry
    val = val % 10

    # Result of this node is now val
    result = ListNode(val)

    # If there is nothing to do, then return the last node
    # Nothing to do if there is no next node, and there is no carry
    if l1.next == None and l2.next == None and carry == 0:
        return result;

    # l1next and l2next are the next nodes if they exist, otherwise fill them
    # with a 0 node
    l1next = l1.next if l1.next != None else ListNode(0)
    l2next = l2.next if l2.next != None else ListNode(0)

    # Add the two nodes and carry
    result.next = self.addTwoNumbers(l1next, l2next, carry)
    return result

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print result.val,
  result = result.next
# 7 0 8
