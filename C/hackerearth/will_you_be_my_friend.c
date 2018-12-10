/* Max feels lonely after shifting to a new locality, as he does not have any friend there. So his parents bought him a new number from the 
Integers SuperMarket! Every child in the locality has bought a number from the same market.
He takes the number to go play with other children in the locality. But to his surprise, there is a rule in the locality, two people A and B 
can only be considered friends if numbers with A and B are not Coprime, i.e they have a common factor other than 1.
You are given the number that Max bought and the numbers of other children in the locality. Can you find how many friends he can have?
Input:
First line contains an integer A, the number that Max has.
Second line contains N, the count of children in the locality.
Third line contains N space-separated integers, where Xi is the integer with the ith child.
Output:
Output the maximum number of friends that Max can make. 

SAMPLE INPUT
6
3
4 7 12
SAMPLE OUTPUT
2
*/
#include <stdio.h>
int main(){
    int x,n;
    scanf("%d %d",&x,&n);
    int a[n],i,f=0;
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    for(i=0;i<n;i++){
        for(int j=2;j<x/2;j++){
            if(a[i]%j==0 && x%j==0){
                f++;
                break;
            }
        }
    }
    printf("%d",f);
    return 0;
}