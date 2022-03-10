"""You are given the pointer to the head node of a sorted linked list, where the data in the nodes is in ascending order.
Delete nodes and return a sorted list with each distinct value in the original list. The given head pointer may be null indicating that the list is empty.
"""

def removeDuplicates(llist):
    # Write your code here
    temp = llist
    
    while(temp.next != None):
        if temp.data == temp.next.data:
            temp.next = temp.next.next
            continue
        temp = temp.next
    return llist
