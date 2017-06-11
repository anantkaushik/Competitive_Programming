/* Dhananjay has recently learned about ASCII values.He is very fond of experimenting. 
With his knowledge of ASCII values and character he has developed a special word and named it Dhananjay's Magical word.
A word which consist of alphabets whose ASCII values is a prime number is an Dhananjay's Magical word. 
An alphabet is Dhananjays Magical alphabet if its ASCII value is prime.
Dhananjay's nature is to boast about the things he know or have learnt about. 
So just to defame his friends he gives few string to his friends and ask them to convert it to Dhananjay's Magical word. 
None of his friends would like to get insulted. Help them to convert the given strings to Dhananjay's Magical Word.
Rules for converting:
1.Each character should be replaced by the nearest Dhananjay's Magical alphabet.
2.If the character is equidistant with 2 Magical alphabets. The one with lower ASCII value will be considered as its replacement.
Input format:
First line of input contains an integer T number of test cases. Each test case contains an integer N (denoting the length of the string) 
and a string S.
Output Format:
For each test case, print Dhananjay's Magical Word in a new line.

SAMPLE INPUT
1
6
AFREEN

SAMPLE OUTPUT
CGSCCO
*/
#include <stdio.h>
int main(){
    int t,n,i;
    int p[12]={67,71,73,79,83,89,97,101,103,107,109,113};
    scanf("%d",&t);
    while(t>0){
        scanf("%d",&n);
        char s[n];
        int d1,d2;
        scanf("%s",s);
        for(i=0;i<n;i++){
            if(s[i]<=69)
                s[i]=67;
            else if(s[i]>=113)
                s[i]=113;
            else {
                int j=0;
                for(;j<12;j++){
                    if(p[j]>s[i]){
                        d1=p[j]-s[i];
                        d2=s[i]-p[j-1];
                        if(d1<d2){
                            s[i]=p[j];
                            break;
                        }
                        else{
                            s[i]=p[j-1];
                            break;
                        }
                    }
                }
            }
        }
        for(i=0;i<n;i++)
            printf("%c",s[i]);
        printf("\n");
        t--;
    }
    return 0;
}