/* You have been given an array A of size N consisting of positive integers. 
You need to find and print the product of all the number in this array Modulo 109+7

Input Format: The first line contains a single integer N denoting the size of the array. 
The next line contains N space separated integers denoting the elements of the array

Output Format: Print a single integer denoting the product of all the elements of the array Modulo 109+7

Sample Input: 
5
1 2 3 4 5

Sample Output: 120 */

#include <stdio.h>
int main(){
    int n;
    long int product=1;
    scanf("%d",&n);
    int a[n];
    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
        product=(product*a[i]) % (1000000007);
    }
    printf("%ld",product);
    return 0;
}