/*You are given two numbers a and b. Your task is to find the sum of two numbers.
Input:The first line contains an integer t, denoting the number of test cases. Next t lines contain two integers, a and b separated by a space.*/
//Practice question from hackerearth.

#include <stdio.h>
void main(){
    int cases,a,b;
    scanf("%d",&cases);
    while(cases!=0){
        scanf("%d %d",&a,&b);
        printf("%d\n",a+b);
        cases--;
    }
}
