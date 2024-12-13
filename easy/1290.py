# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        values = []
        converted = 0
        
        while head:
            values.append(head.val)
            head = head.next

        for i in range(len(values)):
            converted += values[i] * 2 ** (len(values) - i - 1)

        return converted