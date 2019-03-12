"""
Problem Link: https://practice.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1

Given a linked list of N nodes. The task is to remove duplicates from the given list (if exists).

For example if the linked list is 11->11->11->21->43->43->60, then linked list should be converted to 11->21->43->60.

Note: Try not to use extra space. Expected time complexity is O(N).

Input:
First line of input contains number of testcases T. 
For each testcase, first line of input contains length of linked list and next line contains the linked list data.

Output:
For each testcase, there will be a single line of output which contains linked list with no duplicates.

User Task:
The task is to complete the function removeDuplicates() which should remove the duplicates from linked list.

Constraints:
1 <= T <= 100
1 <= N <= 100

Example:
Input
2
4
2 2 4 5
5
2 2 2 2 2

Output
2 4 5
2

Explanation:
Testcase 1: In the given linked list 2 ->2 -> 4-> 5, only 2 occurs more than 1 time.
"""
class node:
    def __init__(self):
        self.data = None
        self.next = None
class Linked_List:
    def __init__(self):
        self.head = None
    def get_head(self):
        return self.head
    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node
def printlist(ptr):
    while ptr!=None:
        print(ptr.data, end=" ")
        ptr= ptr.next
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        newHead = None
        newHead = removeDuplicates(list1.get_head())
        printlist(newHead)
        print('')
''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# Your task is to complete this function
# Function should return head to the new List
def removeDuplicates(head):
    # code here
    node = head
    while node and node.next:
        if node.data == node.next.data:
            node.next = node.next.next
        else:
            node = node.next
    return head