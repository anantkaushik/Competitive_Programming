/* Ash is preparing for his End semester exams and there are total K topics which he has to cover so that he can perform well in it. 
He has decided that he will study the topics sequentially. So, he is going to start from "MONDAY". 
Ash has got a very tight schedule and for each day of the week he already knows how many topics will he be able to study on a particular day.
It is guaranteed that Ash will not skip any day and will follow the routine sincerely, 
Determine on which day of the week will he be able to complete all the topics. (1st day of week is assumed to be MONDAY).
INPUT:-
First line of each test file contains the number of test cases T, Each test case will contain a positive integer K followed by 
array A in the next line which has 7 integers denoting the number of topics which Ash will be able to cover on a particular day of week A[0] 
will be for MONDAY, A[1] will be for TUESDAY ,..., A[6] will be SUNDAY.
OUTPUT:-
For each test case print the day of week in capital letters on which he will complete his syllabus.

SAMPLE INPUT
3
7
1 1 1 1 1 1 1
2
1 1 0 0 0 0 0
10
0 0 0 0 0 0 1

SAMPLE OUTPUT
SUNDAY
TUESDAY
SUNDAY
*/
#include <stdio.h>
int main(){
    int t;
    scanf("%d",&t);
    while(t>0){
        int a[7],i,ans=0;
        long long int sum=0,k;
        char *w[7]={"MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"};
        scanf("%lld",&k);
        for(i=0;i<7;i++){
            scanf("%d",&a[i]);
            sum+=a[i];
        }
        if(k>sum && k%sum==0){
            k=sum;
        }
        else if(k>sum && k%sum!=0)                                                                                                        
            k=k%sum;
        for(i=0;i<7;i++){
            k-=a[i];
            ans=i;
            if(k<=0)
                break;
        }
        printf("%s\n",w[ans]);
        t--;
    }
    return 0;
}