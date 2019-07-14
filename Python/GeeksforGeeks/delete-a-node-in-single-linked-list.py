"""
Problem Link: https://practice.geeksforgeeks.org/problems/delete-a-node-in-single-linked-list/1

Delete xth node from a single linked list. Your task is to complete the method deleteNode which takes two arguments:  
the address of the head of the linked list and an integer x. The function returns the head of the  modified linked list. 

Input:
The first line of input contains an element T, denoting the no of test cases. Then T test cases follow. Each test case contains three lines. 
The first line of each test case contains an integer N denoting the no of elements of the linked list. Then in the next line are N 
space separated values of the linked list. The third line of each test case contains an integer x.

Output:
The output for each test case will be the space separated value of the returned linked list.

Constraints:
1<=T<=300
2<=N<=100
1<=x<=N

Example(To be used only for expected output):

Input:
2
3                       
1 3 4               
3                       
4
1 5 2 9                    
2

Output:
1 3           
1 2 9
"""
{
# Node Class    
class node:
    def __init__(self):
        self.data = None
        self.next = None
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
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
def printlist(head):
    temp = head
    while(temp):
        print(temp.data, end=" ")
        temp = temp.next
    print('')
# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        k = int(input())
        newhead = delNode(list1.head, k)
        printlist(newhead)
}
''' This is a function problem.You only need to complete the function given below '''
# your task is to complete this function
# function should return new head pointer
def delNode(head, k):
    # Code here
    if k == 1:
        return head.next
    cur = head
    k -= 1
    while k > 1:
        cur = cur.next
        k -= 1
    cur.next = cur.next.next
    return head