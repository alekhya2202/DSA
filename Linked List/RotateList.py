#   https://leetcode.com/problems/rotate-list/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        if k == 0:
            return head
        
        if not head: 
            return head
        
        l = self.getLength(head)
        if l == 1 or l == k or k % l == 0:
            return head
        
        rot = l - (k % l) + 1
        
        temp = head
        last = None 
        new_head = None 
        
        i = 1 
        
        while temp: 
            if i + 1 == rot:
                last = temp
            if i == rot:
                new_head = temp
            i += 1
            temp = temp.next
        
        temp = new_head
        while(temp.next != None):
            temp = temp.next
        temp.next = head
        
        temp = new_head
        while(temp != last):
            temp = temp.next
        temp.next = None
        return new_head
        
    def getLength(self,head):
        l = 0 
        while head: 
            l += 1 
            head = head.next 
        return l 
