"""
Given a sorted array with possibly duplicate elements, the task is to find indexes of first 
and last occurrences of an element x in the given array.

Input:
The first line of input contains an integer T denoting the no of test cases. 
Then T test cases follow. Each test case contains an integer N denoting the size of the array. 
Then in the next line are N space separated values of the array. The last line of each 
test case contains an integer x.

Output:
For each test case in a new line print two integers separated by space denoting the first 
and last occurrence of the element x. If the element is not present in the array print -1.

Example:
Input:
2
9
1 3 5 5 5 5 67 123 125
5
9
1 3 5 5 5 5 7 123 125
7
Output:
2 5
6 6
"""
t = int(input()) #no of test cases

def binarysearch(n,nums,target): #function to find last index of element target
        first = 0
        last = n-1
        middle = int((first+last)/2)
        while first<= last:
            if nums[middle] <= target:
                first = middle + 1
            else:
                last = middle - 1
            middle = int((first+last)/2)
            if first > last:
                return first
                
def fbinarysearch(nums,target): #function to find first index of element target
        n = len(nums)
        first = 0
        last = n-1
        middle = int((first+last)/2)
        while first<= last:
            if nums[middle] < target:
                first = middle + 1
            else:
                last = middle - 1
            middle = int((first+last)/2)
            if first > last:
                return first
                
while t > 0: # main function
    n = int(input())
    arr = list(map(int,input().split()))
    target = int(input())
    l = binarysearch(n,arr,target) # finding the last index of the target if present in the list
    if arr[l-1] != target: # checking whether the target exist in the list or not.
        print("-1") #if target is not present in the list
    else:  #if target is present in the list
        f = fbinarysearch(arr[:l],target) # finding the first index of the target
        print(f,l-1)
    t -= 1