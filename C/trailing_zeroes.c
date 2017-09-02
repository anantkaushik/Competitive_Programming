/* Given a number Find the number of trailing zeroes in its factorial.
Input Format: A single integer - N
Output Format: Print a single integer which is the number of trailing zeroes.


SAMPLE INPUT: 10
SAMPLE OUTPUT: 2

Explanation: 10! = 3628800 has 2 zeros in the end. */

#include <stdio.h>
int main(){
    int n,count=0;
    scanf("%d",&n);
    for (int i=5; n/i>=1; i *= 5)
        count += n/i; 
    printf("%d",count);
    return 0;
}