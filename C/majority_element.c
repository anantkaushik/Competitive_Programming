/* Write a program to find the majority element in the array. A majority element in an array A[] of size n is an element that appears more than n/2 
times (and hence there is at most one such element).  If input array doesn't contain a majority element, then output "NO Majority Element"

Input:  The first line of the input contains T denoting the number of testcases. The first line of the test case will be the size of array and 
second line will be the elements of the array.
Output: For each test case the output will be the majority element of the array.

Sample Input:
2
5
3 1 3 3 2
3
1 2 3

Sample Output:
3
NO Majority Element  */
#include <stdio.h>

int main() {
	int t;
	scanf("%d",&t);
	while(t>0){
	    int n;
	    scanf("%d",&n);
	    int a[n],b[101]={0},i,max=-1;
	    for ( i=0; i<n; i++ ) {
	        scanf("%d",&a[i]);
	        b[a[i]]+=1;
	    }
	    for(i=0;i<=100;i++){
	        if(b[i]>n/2)
	            max=i;
	    }
	    if(max>-1)
	        printf("%d\n",max);
	    else
	        printf("NO Majority Element\n");
	    t--;
	}
	return 0;
}