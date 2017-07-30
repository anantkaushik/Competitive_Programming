/* A Krishnamurthy number is a number whose sum of the factorial of digits is equal to the number itself. Given a number N as input.
Write a program to check whether this number is krishnamurthy number or not.
Input:
First line of input contains a single integer T which denotes the number of test cases. Then T test cases follows. 
First line of each test case contains a single integer N.
Output:
For each test case print "YES" without quotes if N is a Krishnamurthy Number otherwise print "NO".

Sample Input:
2
145
235
Sample Output:
YES
NO
*/
#include <stdio.h>

int main() {
	int t;
	scanf("%d",&t);
	while(t>0){
	    int n,x,sd,sum=0;
	    scanf("%d",&n);
	    x=n;
	    while(x>0){
	        sd=x%10;
	        int fact=1;
	        while(sd>0){
	            fact*=sd;
	            sd--;
	        }
	        sum+=fact;
	        x=x/10;
	    }
	    if(n==sum)
	        printf("YES\n");
	    else
	        printf("NO\n");
	    t--;
	}
	return 0;
}