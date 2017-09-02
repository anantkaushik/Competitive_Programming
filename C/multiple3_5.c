/* Find the sum of all the multiples of 3 or 5 below N. 

Input Format: First line contains T that denotes the number of test cases.This is followed by T lines,each containing an integer,N. 
Output Format: For each test case,print an integer that denotes the sum of all the multiples of 3 or 5 below N.
Sample Input:
2
10
100
Sample Output:
23
2318*/
#include <stdio.h>
int main(){
    int t; 
    scanf("%d",&t);
    for(int a0 = 0; a0 < t; a0++){
        long int n,sum=0,p; 
        scanf("%ld",&n);
        p = (n-1)/3;
        sum = ((3*p*(p+1))/2);

        p = (n-1)/5;
        sum = sum + ((5*p*(p+1))/2);

        p = (n-1)/15;
        sum = sum - ((15*p*(p+1))/2);
        printf("%ld\n",sum);
    }
    return 0;
}
