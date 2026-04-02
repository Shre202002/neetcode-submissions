# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        current = dummy
        while l1 or l2 or carry != 0 :
            var1 = l1.val if l1 else 0
            var2 = l2.val if l2 else 0

            total = var1 + var2 + carry
            carry = total //10
            dig = total % 10

            current.next = ListNode(dig)
            current = current.next


            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next



        