/* You are given an integer N. You need to print the series of all prime numbers till N.

Input Format: The first and only line of the input contains a single integer N denoting the number 
till where you need to find the series of prime number.

Output Format: Print the desired output in single line separated by spaces.

Sample Input: 9
Sample Output: 2 3 5 7 */

#include <stdio.h>
int main(){
    int n,a[500],j,i,x,flag=0;
    scanf("%d",&n);
    x=0;
    for(i=2;i<=n;i++){
        for(j=2;j<=i/2;j++){
		    if(i%j==0){
			    flag = 1;
			    break;
		    }
		    else
			    flag = 0;
        }
        if(flag==0){
            a[x]=i;
            x++;
        }
}
    for(i=0;i<x;i++)
        printf("%d ",a[i]);
    return 0;
}
