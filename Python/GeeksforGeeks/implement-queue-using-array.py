"""
Problem Link: https://practice.geeksforgeeks.org/problems/implement-queue-using-array/1

Implement a Queue using Array. Your task is only to complete the functions push and pop.

Input Format:
The first line of the input contains an integer 'T' denoting the number of test cases. Then T test cases follow.
First line of each test case contains an integer Q denoting the number of queries . 
A Query Q is of 2 Types:
(i) 1 x   (a query of this type means  pushing 'x' into the queue)
(ii) 2     (a query of this type means to pop element from queue and print the poped element)
The second line of each test case contains Q queries seperated by space.

Output Format:
The output for each test case will  be space separated integers having -1 if the queue is empty else the element poped out from the queue .

Your Task :
You are required to complete the two methods push which take one argument an integer 'x' to be pushed into the quee  and pop which returns 
a integer poped out from othe queue.

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
2 3

Explanation:
In the first test case for query 
1 2    the quee will be {2}
1 3    the queue will be {2 3}
2       poped element will be 2 the queue will be {3}
1 4    the queue will be {3 4}
2       poped element will be 3
"""
{
#Initial Template for Python 3
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
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
                i=i+1
        print()   

}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
class MyQueue:
    def __init__(self):
        self.queue = []
        
    def push(self, item):
        #add code here
        self.queue.append(item)
    
    def pop(self):
        # add code here
        if not self.queue:
            return -1
        return self.queue.pop(0)