/* Given a number N. You need to write a program to count the number of digits in N which evenly divides N.

Input:
First line of input contains an integer T which denotes the number of test cases. T test cases follows. First line of each test case contains a single integer N.
Output:
For each test case in a new line print the total number of digits of N which evenly divides N.

Sample Input:
3
12
1012
23
Sample Output:
2
3
0 */
#include <stdio.h>

int main() {
	int t;
	scanf("%d",&t);
	while(t>0){
	    int n,x,sd,count=0;
	    scanf("%d",&n);
	    x=n;
	    while(x>0){
	        sd=x%10;
	        if(sd!=0  && n%sd==0)
	            count++;
	        x=x/10;
	    }
	    printf("%d\n",count);
	    t--;
	}
	return 0;
}