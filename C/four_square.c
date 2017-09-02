/* Rahul has recently been obsessed with mathematics, and spends most of his time reading the research notes of his equally eccentric math professor. 
On one of the pages of the research notes, Rahul finds a scribble that says, " the number of ways to represent a number as sum of four squares would be 
the ultimate answer to Life, the Universe and Everything", now since he doesn't have enough time to calculate this for all the numbers, he asks your help.
Given a number N, your task is to print the number of ways it can be represented as sum of four squares.
Input:
First line contains number of test cases T. Next T lines contains a single number N.
Output:
For each test case print number of ways a given N can be represented as the sum of four squares.

SAMPLE INPUT
4
1
2
3
4
SAMPLE OUTPUT
8
24
32
24
*/
#include <stdio.h>
int main(){
    int t;
    scanf("%d",&t);
    while(t>0){
        long long int n,i,j,ans=0;
        scanf("%lld",&n);
        for(i=1;i*i<n;i++){
            if(n%i==0){
                if(i%4!=0)
                    ans+=i;
                j=n/i;
                if(j%4!=0)
                    ans+=j;
            }
        }
        if(i*i==n){
            if(i%4!=0)
                ans+=i;
        }
        ans*=8;
        printf("%lld\n",ans);
        t--;
    }
    return 0;
}