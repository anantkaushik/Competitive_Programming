/* Given two numbers, find the GCD of those 2 numbers.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. 
Each test case contains two space separated integers a and b.
Output:
Print the GCD of the two numbers.

Sample Input:
98 56
48 18
Sample Output:
14
6
*/
#include <stdio.h>
int main(){
    int t;
    scanf("%d",&t);
    while ( t>0 ) {
        int a,b,temp,i;
        scanf("%d %d",&a,&b);
        temp = (a<b?a:b);
        for( i=temp ; i>=1 ; i-- ) {
            if( a % i == 0 && b % i == 0 )
                break;
        }
        printf("%d\n",i);
        t--;
    }
	return 0;
}