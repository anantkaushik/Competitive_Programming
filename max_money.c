/* Given street of houses (a row of houses), each house having some amount of money kept inside; 
now there is a thief who is going to steal this money but he has a constraint/rule that he cannot steal/rob two adjacent houses. 
Find the maximum money he can rob.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N and money.

Output: Print maximum money he can rob.

Sample Input:
2
5 10
2 12

Output:
30
12
*/
#include <stdio.h>
int main(){
    int t;
    scanf("%d",&t);
    while ( t>0 ) {
        int n,a;
        scanf("%d %d",&n,&a);
        if ( n%2==0 )
            n=n/2;
        else
            n=(n/2)+1;
        printf("%d\n",n*a);
        t--;
    }
	return 0;
}