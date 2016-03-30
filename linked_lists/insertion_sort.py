# Needs Review
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def insertionSortList(self, A):
		if not A or not A.next:
			return A
		res = ListNode(0)
		res.next = A
		while A.next:
			A = A.next
		prev = self.getPrev(res, A)
		while prev:
			temp = prev
			while (A.next and A.val > A.next.val):
				self.exchange(prev, A, A.next)	# A moves to next position
				prev = prev.next
			A = temp
			prev = self.getPrev(res, A)
		return res.next
	def exchange(self, prev, node, next):
		if prev:
			prev.next = next
		node.next = next.next
		next.next = node
		return node
	def getPrev(self, head, node):
		if head == node:
			return None
		while head.next != node:
			head = head.next
		return head
"""
Insertion Sort ListBookmark
Sort a linked list using insertion sort.

We have explained Insertion Sort at Slide 7 of Arrays

Insertion Sort Wiki has some details on Insertion Sort as well.

Example :

Input : 1 -> 3 -> 2

Return 1 -> 2 -> 3
"""
