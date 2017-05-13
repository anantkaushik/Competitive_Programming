/*Given an integer 1 <= N <= 3000, you have to print the Nth prime number.

SAMPLE INPUT: 3

SAMPLE OUTPUT: 5 */

#include <stdio.h>
int main(){
    int n,count=0,flag=0,no;
    scanf("%d",&n);
    for(int i=2;;i++){
        for(int j=2;j<=i/2;j++){
            if(i%j==0){
                flag=1;
                break;
            }
            else
                flag=0;
        }
        if(flag==0)
            count++;
        else if(count==n){
            no=i-1;
            break;
        }
    }
    printf("%d",no);
    return 0;
}