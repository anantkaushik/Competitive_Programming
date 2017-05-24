/* Bob is fond of the number 3. He was given n numbers and he decides to count all the multiples of 3 from the n numbers. 
You have to write a program to help Bob.

INPUT:
1. The first line of input contains the integer n.
2. Then n lines follow, each containing a positive integer a[i], 1<=i<=n.

OUTPUT: The output contains a single integer, the required count. 

SAMPLE INPUT
10
1 
2 
3 
4 
5 
6 
7 
8 
9 
10

SAMPLE OUTPUT
3
*/
#include <stdio.h>
int main(){
    int n,count=0;
    scanf("%d",&n);
    long long int a[n];
    for(int i=0;i<n;i++){
        scanf("%lld",&a[i]);
        if(a[i]%3==0)
            count++;
    }
    printf("%d",count);
    return 0;
}