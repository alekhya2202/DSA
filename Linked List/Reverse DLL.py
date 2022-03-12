#https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem?isFullScreen=true
"""Given the pointer to the head node of a doubly linked list, reverse the order of the nodes in place. 
That is, change the next and prev pointers of the nodes so that the direction of the list is reversed. Return a reference to the head node of the reversed list.

Note: The head node might be NULL to indicate that the list is empty."""

def reverse(llist):
    # Write your code here
    ptr1 = llist
    ptr2 = ptr1.next
    
    ptr1.next = None
    ptr1.prev = ptr2
    
    while(ptr2 != None):
        ptr2.prev = ptr2.next
        ptr2.next = ptr1
        ptr1 = ptr2
        ptr2 = ptr2.prev
    
    return ptr1
