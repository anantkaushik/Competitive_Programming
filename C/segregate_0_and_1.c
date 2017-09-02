/* You are given an array of 0s and 1s in random order. Segregate 0s on left side and 1s on right side of the array.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N,N is the size of array.
The second line of each test case contains N input C[i].

Output:
Print 0s on left side and 1s on right side.

Sample Input:

2
5
0 0 1 1 
4
1 1 1 1

Sample Output:
0 0 0 1 1
1 1 1 1
*/
#include <stdio.h>
int main(){
    int t;
    scanf("%d",&t);
    while ( t>0 ) {
        int n;
        scanf("%d",&n);
        int a[n],count=0,i;
        for ( i=0 ; i<n ; i++ ) {
            scanf("%d",&a[i]);
            if(a[i]==0)
                count++;
        }
        for( i=0 ; i<n ; i++ ) {
            if ( i < count )
                printf("0 ");
            else
                printf("1 ");
        }
        printf("\n");
        t--;
    }
	return 0;
}