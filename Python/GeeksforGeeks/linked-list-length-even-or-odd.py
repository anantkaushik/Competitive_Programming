"""
Problem Link: https://practice.geeksforgeeks.org/problems/linked-list-length-even-or-odd/1

Given a linked list of size N, your task is to complete the function isLengthEvenOrOdd() which contains head of the linked list and check whether the 
length of linked list is even or odd.

Input:
The input line contains T, denoting the number of testcases. Each testcase contains two lines. the first line contains N(size of the linked list). 
The second line contains N elements of the linked list separated by space.

Output:
For each testcase in new line, print "even"(without quotes) if the length is even else "odd"(without quotes) if the length is odd.

User Task:
Since this is a functional problem you don't have to worry about input, you just have to  complete the function isLengthEvenOrOdd().

Constraints:
1 <= T <= 100
1 <= N <= 103
1 <= A[i] <= 103

Example:
Input:
2
3
9 4 3
6
12 52 10 47 95 0

Output:
Odd
Even

Explanation:
Testcase 1: The length of linked list is odd.
"""
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
    def insert(self, val):
        if self.head == None:
            self.head = node(val)
        else:
            new_node = node(val)
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node
def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head = createList(arr, n)
        if(isLengthEvenOrOdd(head)):
            print('Even')
        else:
            print('Odd')


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# your task is to complete this function
# function should return true/1 if length is even
# else return false/0
def isLengthEvenOrOdd(head):
    # Code here
    fast = head
    while fast and fast.next:
        fast = fast.next.next
    return (fast == None)