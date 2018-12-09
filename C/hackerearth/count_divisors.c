/* You have been given 3 integers-l,r & k.Find how many numbers b/w l & r (both inclusive) are divisible by k. 
You do not need to print these numbers, you just have to find their count.

Input Format :The first and only line of input contains 3 space separated integers l,r and k

Output Format: Print the required answer on a single line. 

Sample Input: 1 10 1
Sample Output: 10 */
#include <stdio.h>

int main(){
    int l,r,k,count=0;
    scanf("%d %d %d",&l,&r,&k);
    for(int i=l;i<=r;i++){
        if(i%k==0)
            count++;
    }
    printf("%d",count);
    return 0;
}