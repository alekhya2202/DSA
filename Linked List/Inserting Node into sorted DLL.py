#https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem?isFullScreen=true
#Given a reference to the head of a doubly-linked list and an integer, , create a new DoublyLinkedListNode object having data value  
#and insert it at the proper location to maintain the sort.

def sortedInsert(llist, data):
    # Write your code here
    node = DoublyLinkedListNode(data)
    head = llist
    
    if head.data > data:
        node.next = head
        node.prev = None
        head.prev = node
        return node
        
    while(head.data <= data and head.next != None and head.next.data <= data):
        head = head.next
        
    node.prev = head
    node.next = head.next
    head.next = node
    if node.next != None:
        node.next.prev = node
    
    return llist
