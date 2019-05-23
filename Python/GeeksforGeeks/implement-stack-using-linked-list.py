"""
Problem Link: https://practice.geeksforgeeks.org/problems/implement-stack-using-linked-list/1

Implement a Stack using Linked List .

Input Format:
The first line of the input contains an integer 'T' denoting the number of test cases. Then T test cases follow.
First line of each test case contains an integer Q denoting the number of queries . 
A Query Q is of 2 Types
(i) 1 x   (a query of this type means  pushing 'x' into the stack)
(ii) 2     (a query of this type means to pop element from stack and print the poped element)
The second line of each test case contains Q queries seperated by space.

Output Format:
The output for each test case will  be space separated integers having -1 if the stack is empty else the element poped out from the stack . 
You are required to complete the two methods push which take one argument an integer 'x' to be pushed into the stack  and pop which 
returns a integer poped out from the stack.

Your Task:
Since this is a function problem, you don't need to take any input. Just complete the provided function.

Constraints:
1 <= T <= 100
1 <= Q <= 100
1 <= x <= 100

Example:
Input
1
5
1 2 1 3 2 1 4 2  
Output
3 4

Explanation:
In the first test case for query 
1 2    the stack will be {2}
1 3    the stack will be {2 3}
2       poped element will be 3 the stack will be {2}
1 4    the stack will be {2 4}
2       poped element will be 4
"""
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=Stack()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
        print()

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# Class to represent a node 
class StackNode: 
	# Constructor to initialize a node 
	def __init__(self, data): 
		self.data = data 
		self.next = None
		
class Stack: 
    
    # The method push to push element into 
    # the stack
    def __init__(self):
        self.head = None
        
    def push(self, data): 
        #Add code here
        if not self.head:
            self.head = StackNode(data)
            return 
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = StackNode(data)
        
    # The method pop which return the element 
    # poped out of the stack
    def pop(self):
        #Add code here
        if not self.head:
            return -1
        cur = self.head
        if not cur.next:
            val = cur.data
            self.head = None
            return val
        while cur.next.next:
            cur = cur.next
        val = cur.next.data
        cur.next = None
        return val