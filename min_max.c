/*Given an array of integers . Check if all the numbers between minimum and maximum number in array exist's within the array .
Print 'YES' if numbers exist otherwise print 'NO'(without quotes).

Input:Integer N denoting size of array
Next line contains N space separated integers denoting elements in array

Output:Output your answer */

/* Sample Input:
6
4 2 1 3 5 6
Sample Output:
YES */
#include <stdio.h>
int main(){
    int size,flag;
    scanf("%d",&size);
    int a[size],i,j,max=0,min=9999;
    for(i=0;i<size;i++){
        scanf("%d",&a[i]);
        if(a[i]<min)
            min=a[i];
        else if(a[i]>max)
            max=a[i];
    }
    for(i=min;i<=max;i++){
        flag=0;
        for(j=0;j<size;j++)
            if(a[j]==i){
                flag=1;
                break;
            }
        if(flag==0)
            break;
    }
    if(flag==1)
        printf("YES");
    else
        printf("NO");
    return 0;
}