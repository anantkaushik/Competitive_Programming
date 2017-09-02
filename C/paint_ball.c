/* Bob got a new contract of painting wall. Wall has N bricks. Bob can paint each brick with three type of colors : Type A, Type B and Type C. 
Assume Bob has enough amount of paints of all three types. Find number of ways Bob can paint the wall having N bricks with color of Type A, 
Type B and Type C such that no two adjacent brick should have same color.
Input:
First line of input contains number of test cases T. Each test case contains a single integer N, number of bricks in wall.
Output:
For each test case print the number of ways Bob can paint the wall. Answer can be too large print answer modulo 109+7. 

SAMPLE INPUT
2
1
5
SAMPLE OUTPUT
3
48
*/
#include <stdio.h>
#define mod 1000000007
long int max[100001];
void value(){
    max[0]=3;
    for(int i=1;i<100001;i++)
        max[i]=(max[i-1]*2)%mod;
}
int main(){
    int t;
    scanf("%d",&t);
    value();
    while(t>0){
        long int n;
        scanf("%ld",&n);
        printf("%ld\n",max[n-1]);
        t--;
    }
    return 0;
}