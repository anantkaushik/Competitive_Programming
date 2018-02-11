/*This time your task is simple.

Given two integers X and K, find the largest number that can be formed by changing digits at atmost 
K places in the number X

Input:
First line of the input contains two integers X and K separated by a single space.

Output:
Print the largest number formed in a single line.

SAMPLE INPUT 
4483 2

SAMPLE OUTPUT 
9983
*/
#include <stdio.h>
int main(){
    int n,a[1000000],i=0;
    char c;
    while((c=getchar())!=32){
        a[i]=c-48;
        i++;
    }
    scanf("%d",&n);
    int k=0;
    while(k<i){
        if(a[k]!=9 && n>0){
            printf("9");
            n--;
        }
        else
            printf("%d",a[k]);
        k++;
    }
    return 0;
}