/* You have been given a positive integer N. You need to find and print the Factorial of this number. 

Input Format: The first and only line of the input contains a single integer N denoting the number whose factorial you need to find.
Output Format: Output a single line denoting the factorial of the number N.

Sample Input: 2
Sample Output: 2 */

#include <stdio.h>
int main(){
    int n,fact=1;
    scanf("%d",&n);
    while(n>0){
        fact=fact*n;
        n--;
    }
    printf("%d",fact);
    return 0;
}