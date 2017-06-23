/* Little chandu is very fond of playing games. Recently, He found a few straws each of length 1 inches in the store room. 
He took all of them and decided to mark a rectangular area on the floor with straws and warn rest of the family members to not to enter that area 
so that he can play in peace. He wants to maximize that area. But, unable to do so, He seeks for your help. You being the elder brother of chandu, 
write a program for him to find maximum area that he can cover in inches using N straws.
Input: First line of input contains an integer t. then, t lines follow each containing a single integer N- No of straws.
Output:Print the area of largest rectangle that can be formed using the given sticks.

SAMPLE INPUT
3
6
9
11
SAMPLE OUTPUT
2
4
6
*/
#include <stdio.h>
int main(){
    int t;
    scanf("%d",&t);
    while(t>0){
        long long int n,temp,l,b;
        scanf("%lld",&n);
        temp=n/2;
        l=temp/2;
        b=temp-l;
        printf("%lld\n",l*b);
        t--;
    }
    return 0;
}