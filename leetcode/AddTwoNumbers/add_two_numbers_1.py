from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        current_node = result
        carry = 0
        
        while l1 or l2 or carry:
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            carry, remainder = divmod(sum, 10)
            newNode = ListNode (remainder)
            current_node.next = newNode
            current_node = current_node.next
        
        return result.next

if __name__ == '__main__':
    s = Solution()