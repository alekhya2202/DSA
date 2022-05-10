# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def removeNthFromEnd(self, A, B):
        temp = A
        n = 0
        while(temp):
            n += 1
            temp = temp.next
        temp = A
        if B >= n:
            return A.next
        if n == 1:
            return None
        start = n - B - 1
        for i in range(start):
            if A != None:
                temp = temp.next
        if temp.next != None and temp.next.next != None:
            temp.next = temp.next.next
        else:
            temp.next = None
        return A
