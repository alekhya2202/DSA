#https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem?isFullScreen=true
"""Given a pointer to the head of a linked list and a specific position, determine the data value at that position. 
Count backwards from the tail node. The tail is at postion 0, its parent is at 1 and so on."""

def getNode(llist, positionFromTail):
    # Write your code here
    temp = llist
    len_llist = 0
    while(temp != None):
        len_llist += 1
        temp = temp.next

    temp = llist
    for _ in range(len_llist - positionFromTail - 1):
        temp = temp.next
    return temp.data
