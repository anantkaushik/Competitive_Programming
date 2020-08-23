"""
Problem Link: https://www.interviewbit.com/problems/list-cycle/

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
Try solving it using constant additional space.

Example :
Input : 

                  ______
                 |     |
                 \/    |
        1 -> 2 -> 3 -> 4
Return the node corresponding to node 3. 
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        slow = fast = A
        while fast and fast.next:
            if slow == fast:
                break
            slow = slow.next
            fast = fast.next.next
        
        if not fast or fast.next:
            return None
        fast = A
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
