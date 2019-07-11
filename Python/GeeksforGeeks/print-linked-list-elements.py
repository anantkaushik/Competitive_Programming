"""
Problem Link: https://practice.geeksforgeeks.org/problems/print-linked-list-elements/1

You are given the pointer to the head node of a linked list. You have to print all of its elements in order in a single line.
 
Input:
You have to complete a method which takes one argument: the head of the linked list. You should not read any input from stdin/console. 
The struct Node has a data part which stores the data and a next pointer which points to the next element of the linked list. 
There are multiple test cases. For each test case, this method will be called individually.

Output:
Print the elements of the linked list in a single line separated by a single space.

Example:
Input
2
2
1 2
1
4

Output
1 2
4

To be used only for expected output :
Here the first line denotes an integer 'T' the no of test cases and the next line denotes 'N' the no of nodes of linked list.
Then the line after that contains N space separated integers denoting the values of the nodes of the linked list .
"""
{
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
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        llist = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            llist.insert(i)
        printlist(llist.get_head())
        print('')
}
''' This is a function problem.You only need to complete the function given below '''
#Your task is to complete this function
#Your function should print the data in one line only
#You need not to print new line
def printlist(node):
    #code here
    while node:
        print(node.data,end=' ')
        node = node.next