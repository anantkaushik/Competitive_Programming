"""
Problem Link: https://www.interviewbit.com/problems/reverse-linked-list/

Reverse a linked list. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL,
return 5->4->3->2->1->NULL.
"""
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        head = None
        while A:
            A.next, A, head = head, A.next, A
        return head
