/* Given a decimal number. Write a program to convert it into equivalent binary number.
Input:
First line of input contains a single integer T which denotes the number of test cases. 
First line of each test case contains a single integer N which represents a decimal value.
Output:
For each test case, print the binary equivalent of the given decimal value N.
Constraints:
1<=T<=100
1<=N<=100

Sample Input:
3
7
10
33
Sample Output:
111
1010
100001  */	
#include <stdio.h>

int main() {
	int t;
	scanf("%d",&t);
	while (t>0) {
	    int n;
	    scanf("%d",&n);
	    int a[7],i=0;
	    while (n>1) {
	        a[i]= n%2;
	        i++;
	        n=n/2;
	    } 
	    a[i]=1;
	    for (; i>= 0 ; i--)
	        printf("%d",a[i]);
	    printf("\n");
	    t--;
	}
	return 0;
}