/* The Monk wants to buy some cities. To buy two cities, he needs to buy the road connecting those two cities. 
Now, you are given a list of roads, bought by the Monk. You need to tell how many cities did the Monk buy.
Input:
First line contains an integer T, denoting the number of test cases. The first line of each test case contains an integer E, 
denoting the number of roads. The next E lines contain two space separated integers X and Y, denoting that there is an road between city X and city Y.
Output:
For each test case, you need to print the number of cities the Monk bought.

SAMPLE INPUT
1
3
1 2
2 3
1 3
SAMPLE OUTPUT
3
*/
#include <stdio.h>
int main(){
    int t;
    scanf("%d",&t);
    while(t>0){
        int r,j=0;
        int e[20000];
        scanf("%d",&r);
        for(int i=0;i<r;i++){
            int xflag=0,yflag=0,x,y;
            scanf("%d %d",&x,&y);
            if(i==0){
                if(x==y){
                    e[j]=x;
                    j++;
                }
                else{
                    e[j]=x;
                    j++;
                    e[j]=y;
                    j++;
                }
            }
            else{
                for(int c=0;c<j;c++){
                    if(x==e[c])
                        xflag=1;
                    if(y==e[c])
                        yflag=1;
                }
                if(xflag==0 && x!=y){
                    e[j]=x;
                    j++;
                }
                if(yflag==0){
                    e[j]=y;
                    j++;
                }
            }
        }
        printf("%d\n",j);
        t--;
    }
    return 0;
}