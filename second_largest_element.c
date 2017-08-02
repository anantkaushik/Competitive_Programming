/* Given an array of elements. Your task is to find the second maximum element in the array.
Input:
The first line of input contains an integer T which denotes the number of test cases. Then T test cases follows. 
First line of each test case contains a single integer N which denotes the number of elements in the array. 
Second line of each test case contains N space separated integers which denotes the elements of the array.
Output:
For each test case in a new line print the second maximum element in the array. If there does not exist any second largest element, then print -1.

Sample Input:
2
5
2 4 5 6 7
6
7 8 2 1 4 3
Sample Output:
6
7
*/
#include<stdio.h>
int main(){
    int t;
    scanf("%d",&t);
    while(t>0){
        int n;
        scanf("%d",&n);
        int a[n],max=0,temp,i,j;
        for(i=0;i<n;i++){
            scanf("%d",&a[i]);
            if(a[i]>max){
                max=a[i];
            }
        }
        for(i=0;i<n-1;i++){
            for(j=0;j<n-i-1;j++){
                if(a[j]>a[j+1]){
                    temp=a[j];
                    a[j]=a[j+1];
                    a[j+1]=temp;
                }
            }
        }
        for(i=0;i<n;i++){
            if(a[i]==max)
                break;
        }
        printf("%d\n",(i>0?a[i-1]:-1));
        t--;
    }
	return 0;
}