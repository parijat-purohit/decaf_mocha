# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dh = ListNode(0)
        current = dh

        while(list1 and list2):
            if list1.val<list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next
        current.next = list1 or list2
        return dh.next

"""
Exmple of constructing two sorted linked lists.
This also call the function above.

l1 = ListNode(1)
l2 = ListNode(2)

l1.next = l2

l4 = ListNode(1)
l5 = ListNode(3)
l6 = ListNode(4)
l7 = ListNode(7)

l4.next = l5
l5.next = l6
l6.next = l7

s = Solution()
print(s.mergeTwoLists(l1, l4))
"""
"""
The time complexity of the mergeTwoLists function is O(n),
where n is the total number of nodes in the two input lists.
This is because we need to iterate through each node in the
two input lists exactly once, comparing their values and creating
a new node for the merged list if necessary.

The space complexity is also O(n), because we need to create a new
linked list with potentially n nodes in the worst case. However, we
don't need to allocate any additional memory beyond the space required
for the output linked list, so the space complexity is constant with respect
to the input size.
"""
