/* Monk loves to preform different operations on arrays,and so being the principal of Hackerearth School, 
he assigned a task to his new student Mishki. Mishki will be provided with an integer array A of size N and an integer K, 
where she needs to rotate the array in the right direction by K steps and then print the resultant array. 
As she is new to the school, please help her to complete the task.

Input:
The first line will consists of one integer T denoting the number of test cases.
For each test case:
1) The first line consists of two integers N and K, N being the number of elements in the array and K denotes the number of steps of rotation.
2) The next line consists of N space separated integers , denoting the elements of the array A
Output:
Print the required array

SAMPLE INPUT
1
5 2
1 2 3 4 5

SAMPLE OUTPUT
4 5 1 2 3  */

#include <stdio.h>
int main(){
    int t;
    scanf("%d",&t);
    while(t>0){
        int n,k,i;
        scanf("%d %d",&n,&k);
        if(k>n)
            k = k % n;
        int a[n];
        if(k==n || k==0){
            for(i=0;i<n;i++)
                scanf("%d",&a[i]);
        }
        else{
            for(i=k;i<n;){
                if(i<n-1 && i>=k){
                    scanf("%d",&a[i]);
                    i++;
                }
                else if(i==n-1){
                    scanf("%d",&a[i]);
                    i=0;    
                }
                else if(i>=0 && i<k){
                    scanf("%d",&a[i]);
                    if(i==k-1)
                        break;
                    else 
                        i++;
                }
            }
        }
        for(i=0;i<n;i++)
            printf("%d ",a[i]);
        printf("\n");
        t--;
    }
    return 0;
}