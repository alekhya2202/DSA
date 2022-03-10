#https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem?isFullScreen=true
"""Given pointers to the head nodes of  linked lists that merge together at some point, find the node where the two lists merge. The merge point is where both lists point to the same node, i.e. they reference the same memory location. 
It is guaranteed that the two head nodes will be different, and neither will be NULL. If the lists share a common node, return that node's data value."""


def findMergeNode(head1, head2):
    while head1:
        node = head2
        while node:
            if head1 == node:
                return head1.data
            node = node.next
        head1 = head1.next
