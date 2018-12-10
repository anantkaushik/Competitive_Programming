/* After setting up the area. Chandu wanted all his toys to be stacked there in that area. So that all of them are accessible easily. 
Currently, He is having N stacks of toys each with height H1,H2...Hn (assuming all toys are of same height).Chandu did not like the configuration much and 
want to change the height of each stack. To increase the height of a particular stack he can add some toys to it and to decrease the height he can take 
out some toys from that stack. Chandu, knows that he requires X units of effort for putting up an item onto the stack and Y units of effort for removing it. 
Help, chandu in setting up his toys.
Input:First Line of input contains an integer t, which is the number of test cases. then, t lines follow where first line of each test case contains 
three integers N, X and Y then N lines follow containing two integers each a[i] and b[i] (Initial height of ith stack and final height of ith stack.)
Output:Output an integer which is the minimum effort required.
NOTE: he just need to make stacks of given height. Not necessarily each stack should be made from its corresponding stack. 

SAMPLE INPUT
1
3 6 4
3 1
1 2
1 2
SAMPLE OUTPUT
10

Explanation: Here, He is having 3 stacks initially of height 3,1 and 1 He can take out one toy from first stack to get a stack with two toys 
with 4 units of effort. He can put toy on second stack to get a stack with two toys with 6 units of effort. Total effort = 10 units. 
After the two operations he will have three stacks with required heights. */
#include <stdio.h>
#include <string.h>
void quicksort(int arr[],int beg,int last){
    if(beg<last){
    	int pivot=arr[last],count=beg,temp,i;
    	for(i=beg;i<last;i++){	
    	    if(arr[i]<=pivot){
    			temp=arr[i];
    			arr[i]=arr[count];
    			arr[count]=temp;
    			count++;
    		}
    	}
    	temp=arr[last];
    	arr[last]=arr[count];
    	arr[count]=temp;
    	quicksort(arr,beg,count-1);
    	quicksort(arr,count+1,last);
    }
}
int main(){
    int t;
    scanf("%d",&t);
    while(t>0){
        int n,x,y,i;
        scanf("%d %d %d",&n,&x,&y);
        int a[n],b[n],effort=0;
        for(i=0;i<n;i++)
            scanf("%d %d",&a[i],&b[i]);
        quicksort(a,0,n-1);
        quicksort(b,0,n-1);
        for(i=0;i<n;i++){   
            if(a[i]>=b[i])
                effort+=(a[i]-b[i])*y;
            else
                effort+=(b[i]-a[i])*x;
        }
        printf("%d\n",effort);
        t--;
    }
    return 0;
}