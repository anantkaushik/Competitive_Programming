/* Having a good previous year, Monk is back to teach algorithms and data structures. 
This year he welcomes the learners with a problem which he calls "Welcome Problem". 
The problem gives you two arrays A and B (each array of size N) and asks to print new array C such that:
C[i]=A[i]+B[i] ; 1≤i≤N

Input:
First line consists of an integer N,denoting the size of A and B.
Next line consists of N space separated integers denoting the array A.
Next line consists of N space separated integers denoting the array B

Output: Print N space separated integers denoting the array C.

SAMPLE INPUT
5
1 2 3 4 5
4 5 3 2 10

SAMPLE OUTPUT
5 7 6 6 15 */
#include <stdio.h>
int main(){
    int n;
    scanf("%d",&n);
    int a[n],b[n],c[n],i;
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    for(i=0;i<n;i++){
        scanf("%d",&b[i]);
        c[i] = a[i] + b[i];
        printf("%d ",c[i]);
    }
    return 0;
}