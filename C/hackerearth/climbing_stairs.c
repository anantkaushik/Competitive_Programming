/* Alice is climbing stairs. There are total N stairs. She climbs A stairs upwards in day and she comes downstairs in night by B stairs. 
Find number of days she will take to reach the top of staircase.
Input:
First and only line contains three space separated integers denoting A, B, N.
Output:
Print only one line of output denoting the answer to the question.

SAMPLE INPUT
5 1 6
SAMPLE OUTPUT
2
*/
#include <stdio.h>
int main(){
    int a,b,n,days=0,s;
    scanf("%d %d %d",&a,&b,&n);
    s=n%a;
    days=n/a;
    s=s+days*b;
    while(s>0){
        s-=a;
        days++;
        if(s>0)
            s+=b;
    }
    printf("%d",days);
    return 0;
}