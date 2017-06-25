/* Fatland is a town that started with N distinct empires, namely empires 1, 2, ..., N. But over time, the armies of some of these empires 
have taken over other ones. Each takeover occurred when the army of empire i invaded empire j. After each invasion, all of empire j became 
part of empire i, and empire j was renamed as empire i.Empire Huang, leader of Badland, wants to invade Fatland. To do this, he needs to calculate 
how many distinct empires still remain in Fatland after all the takeovers. Help him with this task.

Input:
The first line contains an integer N, the number of empires that were originally in Fatland.
The second line contains an integer K, denoting the number of takeovers that took place.
Each of the next K lines contains 2 space-separated integers i, j, representing that the army of empire i took over that of empire j. 
As a result, empire j does not exist anymore and is now renamed as empire i. It is guaranteed that empire i still exists.
Output: Output one integer, the number of empires that exist in Fatland.

SAMPLE INPUT
4
2
1 2
4 1
SAMPLE OUTPUT
2
Explanation:
Fatland started with empires 1, 2, 3, 4. First, empire 1 invaded empire 2, so empire 2 was renamed to empire 1. 
Then, empire 4 invaded empire 1. So what were at the beginning empires 1 and 2 were renamed to empire 4. 
Now, only empires 3 and 4 remain, so the answer is 2.  */
#include <stdio.h>
int main(){
    int n;
    scanf("%d",&n);
    int a[n],t,x,sum=0;
    for(x=0;x<n;x++)
        a[x]=1;
    scanf("%d",&t);
    while(t>0){
        int i,j;
        scanf("%d %d",&i,&j);
        a[j-1]=0;
        t--;
    }
    for(x=0;x<n;x++){
        sum+=a[x];
    }
    printf("%d",sum);
    return 0;
}