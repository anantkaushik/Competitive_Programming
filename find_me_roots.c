/* Bosky needs your help in completing his maths homework today. He has to solve some questions as homework from a book named Jungly Mathematics. 
He knows that Jungly Mathematics contains certain quadratic equations which have imaginary roots. He is not yet introduced to the concept of imaginary 
roots and is only concerned with the questions having real roots. The book contains N quadratic equation of the form a[i]x2+b[i]x+c[i]=0 where a[i]!=0 
and i represents the index of the question. You have to make a program which will take N, a, b and c as input and tell him how many questions he can 
solve out of those N questions (i.e. You have to find how many quadratic equations in the book have real roots).

Input
Input will contain a number N denoting the number of quadratic equations. N line follow, each one consisting of three space separated integers 
a[i], b[i] and c[i] representing the quadratic equation a[i]x2+b[i]x+c[i]=0. where [0<=i<N]
Output
Print a single integer denoting the number of quadratic equations Bosky can solve.

SAMPLE INPUT
2
1 0 -1
1 1 1
SAMPLE OUTPUT
1
*/
#include <stdio.h>
int main(){
    int n,ans=0;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        int a,b,c,temp;
        scanf("%d %d %d",&a,&b,&c);
        temp=(b*b)-(4*a*c);
        if(temp>=0)
            ans++;
    }
    printf("%d",ans);
    return 0;
}